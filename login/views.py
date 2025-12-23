from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from signup.models import HRProfile  # jaha signup ka model hai
from django.contrib.auth.hashers import check_password

class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            hr = HRProfile.objects.get(email=email)
        except HRProfile.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        if check_password(password, hr.password):
            return Response({"message": "Login successful", "hr_name": hr.hr_name})
        else:
            return Response({"error": "Invalid password"}, status=400)
