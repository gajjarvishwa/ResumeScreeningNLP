import os
import csv
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import JobDescription
from .serializers import JDSerializer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class JDCreateView(APIView):
    def post(self, request):
        title = request.data.get("title")
        jd_text = request.data.get("description")

        if not title or not jd_text:
            return Response({"error": "Title and description required"}, status=400)

        # --- no spacy, no skill extraction ---
        jd = JobDescription.objects.create(
            title=title,
            description=jd_text,
            extracted_skills=[],
        )

        return Response({"jd_id": jd.id}, status=201)


class MatchResumeView(APIView):
    def post(self, request):

        jd_id = request.data.get("jd_id")

        try:
            jd = JobDescription.objects.get(id=jd_id)
        except:
            return Response({"error": "Invalid JD ID"}, status=404)

        # READ CSV
        csv_path = os.path.join(settings.BASE_DIR, "data", "resumes.csv")

        if not os.path.exists(csv_path):
            return Response({"error": "CSV not found"}, status=404)

        resume_paths = []
        resume_names = []
        resume_emails = []
        resume_skills = []

        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                resume_paths.append(row["resume_path"])
                resume_names.append(row["name"])
                resume_emails.append(row["email"])
                resume_skills.append(row["skills"])

        # TF-IDF matching (using resume skills + jd text together)
        corpus = [jd.description] + resume_skills

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(corpus)

        scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

        top5_idx = scores.argsort()[::-1][:5]

        results = []
        for idx in top5_idx:
            results.append({
                "name": resume_names[idx],
                "email": resume_emails[idx],
                "resume_file": "/" + resume_paths[idx],
                "score": int(scores[idx] * 100)
            })

        return Response({"top_5": results})
