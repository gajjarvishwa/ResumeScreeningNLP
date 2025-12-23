from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SendEmailView(APIView):
    def post(self, request):
        candidate_name = request.data.get("name")
        email = request.data.get("email")
        mode = request.data.get("mode")  # accept / reject

        if mode == "accept":
            subject = "Congratulations! You are Selected"
            message = f"Dear {candidate_name},\n\nYou have been selected for the position.\nWe will contact you shortly.\n\nRegards,\nHR Team"
        else:
            subject = "Application Status Update"
            message = f"Dear {candidate_name},\n\nThank you for applying.\nCurrently you are not selected.\n\nRegards,\nHR Team"

        send_mail(
            subject,
            message,
            "yourgmail@gmail.com",   # FROM Email
            [email],
            fail_silently=False
        )

        return Response({"message": "Email sent!"}, status=200)
