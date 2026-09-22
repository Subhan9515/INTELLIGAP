import json

from django.http import JsonResponse
from django.shortcuts import render
from google import genai


def chat(request):

    # Open chatbot page
    if request.method == "GET":
        return render(request, "chatbot/chat.html")


    # Receive message from user
    if request.method == "POST":

        try:

            data = json.loads(request.body)

            message = data.get("message", "").strip()


            # Check empty message
            if not message:

                return JsonResponse(
                    {"error": "Please enter a message."},
                    status=400
                )


            # Connect to Gemini
            client = genai.Client()


            # Generate short AI response
            interaction = client.interactions.create(

                model="gemini-3.8-flash",

                system_instruction=(
                    "You are IntelliGap AI, a student learning assistant. "
                    "Answer in 2 to 5 short lines. "
                    "Use simple words. "
                    "Keep explanations short and clear. "
                    "Give a small example only when necessary. "
                    "Do not give long explanations. "
                    "Help with Python, Java, AI, ML, DBMS, "
                    "HTML, CSS, JavaScript, and academic questions."
                ),

                input=message,
            )


            # Get Gemini answer
            reply = interaction.output_text


            # Send answer to chatbot
            return JsonResponse({
                "reply": reply
            })


        except Exception as e:

            return JsonResponse(
                {"error": str(e)},
                status=500
            )


    # Invalid request
    return JsonResponse(
        {"error": "Invalid request method."},
        status=405
    )