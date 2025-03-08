from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import ChatMessage
from .serializers import ChatMessageSerializer
from groq import Groq

client = Groq()

class ChatbotAPIView(APIView):

    def get(self, request):
        """ Retrieve full chat history for UI """
        chat_history = ChatMessage.objects.all().order_by('timestamp')  # Fetch full history
        serialized_chat = ChatMessageSerializer(chat_history, many=True).data
        return Response({"chat_history": serialized_chat}, status=status.HTTP_200_OK)

    def post(self, request):
        """ Process user message and generate chatbot response """
        user_message = request.data.get('message')

        if not user_message:
            return Response({"error": "Message cannot be empty"}, status=status.HTTP_400_BAD_REQUEST)

        # Savee the user message
        ChatMessage.objects.create(sender="user", message=user_message)

        # Fetch the last 10 messagees for context
        chat_history = ChatMessage.objects.all().order_by('-timestamp')[:10]
        messages = [
            {"role": "user" if msg.sender == "user" else "assistant", "content": msg.message}
            for msg in reversed(chat_history)  # Reverse to maintain order
        ]

        # Generate response using Groq
        completion = client.chat.completions.create(
            model="qwen-2.5-32b",
            messages=messages,
            temperature=0.6,
            max_completion_tokens=1000,
            top_p=0.95,
            stream=False,
            stop=None,
        )

        bot_response = completion.choices[0].message.content.strip()
        clean_response = bot_response.split("</think>\n\n")[-1].strip() if "</think>\n\n" in bot_response else bot_response

        # Save the bot response
        ChatMessage.objects.create(sender="bot", message=clean_response)

        # Fetch full chat history for UI display
        full_chat_history = ChatMessage.objects.all().order_by('timestamp')
        serialized_chat = ChatMessageSerializer(full_chat_history, many=True).data

        return Response({
            "message": clean_response,
            "chat_history": serialized_chat  # Send full history to UI
        }, status=status.HTTP_200_OK)
