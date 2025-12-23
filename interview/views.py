from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Interview
from .serializers import InterviewSerializer
from django.core.mail import send_mail

class ScheduleInterviewView(APIView):
    def post(self, request):
        serializer = InterviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            name = request.data.get("candidate_name")
            email = request.data.get("candidate_email")
            date = request.data.get("date")
            time = request.data.get("time")
            venue = request.data.get("venue")
            mode = request.data.get("mode")

            subject = "Interview Scheduled"
            message = f"""
Hi {name},

Your interview has been scheduled.

📅 Date: {date}
⏰ Time: {time}
📍 Venue: {venue}
💼 Mode: {mode}

Please be available on time.

Regards,
HR Team
"""

            send_mail(
                subject,
                message,
                "your-gmail@gmail.com",
                [email],
                fail_silently=False,
            )

            return Response({"message": "Interview Scheduled & Email Sent!"}, status=200)

        return Response(serializer.errors, status=400)
