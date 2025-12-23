from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import HRUser
from .serializers import HRSignupSerializer


class HRSignupView(APIView):
    def post(self, request):
        serializer = HRSignupSerializer(data=request.data)
        if serializer.is_valid():
            hr = serializer.save()
            return Response({
                "msg": "Signup successful!",
                "email": hr.email
            }, status=201)
        return Response(serializer.errors, status=400)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            hr = HRUser.objects.get(email=email)
        except HRUser.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        if hr.password == password:
            return Response({
                "message": "Login successful",
                "hr_name": hr.hr_name,
                "email": hr.email
            }, status=200)
        else:
            return Response({"error": "Invalid email or password"}, status=400)
