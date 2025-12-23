from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AcceptedCandidate


class SaveAcceptedView(APIView):
    def post(self, request):
        name = request.data.get("name")
        email = request.data.get("email")
        resume = request.data.get("resume")
        score = request.data.get("score")

        if not name or not email:
            return Response({"error": "Missing fields"}, status=400)

        AcceptedCandidate.objects.create(
            name=name,
            email=email,
            resume_file=resume,
            score=score
        )

        return Response({"message": "Saved OK"}, status=200)


class ListAcceptedView(APIView):
    def get(self, request):
        data = AcceptedCandidate.objects.all().order_by("-created_at")

        out = [
            {
                "name": c.name,
                "email": c.email,
                "resume_file": c.resume_file,
                "score": c.score
            }
            for c in data
        ]

        return Response(out, status=200)
