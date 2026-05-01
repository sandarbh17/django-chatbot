from django.urls import path
from .views import chatbot_response, chat_page

urlpatterns = [
    path('chat/', chatbot_response),
     path('', chat_page),
]