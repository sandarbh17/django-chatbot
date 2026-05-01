from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import requests

# 🔑 यहाँ अपनी OpenRouter API key डालो
API_KEY = "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"


def chat_page(request):
    return render(request, "chat.html")


@csrf_exempt
def chatbot_response(request):

    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message")

        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "openai/gpt-3.5-turbo",
                    "messages": [
                        {"role": "user", "content": message}
                    ]
                }
            )

            result = response.json()
            reply = result["choices"][0]["message"]["content"]

        except Exception as e:
            reply = "Error: " + str(e)

        return JsonResponse({"response": reply})

    return JsonResponse({"error": "Invalid request"}, status=400)