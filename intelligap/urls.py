from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('admin/', admin.site.urls),

    # Existing IntelliGap URLs
    path('', include('accounts.urls')),

    # AI Chatbot
    path('chatbot/', include('chatbot.urls')),
]