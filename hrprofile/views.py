from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from signup.models import HRUser
from .serializers import HRProfileSerializer

class HRProfileView(APIView):

    def get(self, request):
        email = request.query_params.get("email")

        try:
            hr = HRUser.objects.get(email=email)
        except HRUser.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        serializer = HRProfileSerializer(hr)
        return Response(serializer.data, status=200)

    def put(self, request):
        email = request.data.get("email")

        try:
            hr = HRUser.objects.get(email=email)
        except HRUser.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        serializer = HRProfileSerializer(hr, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Profile updated successfully!"}, status=200)

        return Response(serializer.errors, status=400)
