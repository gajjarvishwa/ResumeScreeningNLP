import os
import csv
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import ResumeSerializer
from .models import Resume
from .utils import extract_text_from_file, extract_skills_from_text

import re


def extract_email(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    match = re.search(pattern, text)
    return match.group(0) if match else None


def extract_name(text):
    for line in text.split("\n"):
        line = line.strip()
        if line and len(line.split()) <= 5:
            return line
    return None


class ResumeUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        serializer = ResumeSerializer(data=request.data)

        if serializer.is_valid():
            resume = serializer.save()

            try:
                file = request.FILES.get("resume_file")
                if file:

                    # --- CREATE MEDIA/resumes FOLDER ---
                    save_dir = os.path.join(settings.MEDIA_ROOT, "resumes")
                    os.makedirs(save_dir, exist_ok=True)

                    filename = file.name
                    resume_path = os.path.join(save_dir, filename)

                    # --- SAVE FILE ---
                    with open(resume_path, "wb") as dest:
                        for chunk in file.chunks():
                            dest.write(chunk)

                    # --- ONLY PDF ALLOWED ---
                    if not resume_path.lower().endswith(".pdf"):
                        return Response(
                            {"error": "Only PDF files are allowed."},
                            status=status.HTTP_400_BAD_REQUEST
                        )

                    # --- READ FILE AS BYTES ---
                    with open(resume_path, "rb") as f:
                        file_bytes = f.read()

                    # --- EXTRACT TEXT ---
                    text = extract_text_from_file(file_bytes, filename)
                    cleaned_text = text.replace("\r", "").replace("\t", " ").strip()

                    # --- META EXTRACTION ---
                    skills = extract_skills_from_text(cleaned_text)
                    email = extract_email(cleaned_text)
                    name = extract_name(cleaned_text)

                    # --- SAVE TO DATABASE ---
                    resume.resume_file = f"resumes/{filename}"
                    resume.parsed_text = cleaned_text
                    resume.parsed_skills = skills
                    resume.email = email
                    resume.name = name
                    resume.save()

                    # ======================================================
                    # 🔥 AUTO CREATE + APPEND TO CSV
                    # ======================================================
                    csv_dir = os.path.join(settings.BASE_DIR, "data")
                    os.makedirs(csv_dir, exist_ok=True)

                    csv_path = os.path.join(csv_dir, "resumes.csv")

                    file_exists = os.path.isfile(csv_path)

                    with open(csv_path, "a", newline="", encoding="utf-8") as csv_file:
                        writer = csv.writer(csv_file)

                        # header only first time
                        if not file_exists:
                            writer.writerow(["resume_path", "name", "email", "skills"])

                        writer.writerow([
                            f"media/resumes/{filename}",
                            name if name else "",
                            email if email else "",
                            ", ".join(skills) if skills else ""
                        ])

            except Exception as e:
                print("Parsing error:", e)

            return Response({"success": True, "id": resume.id}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
