from django.urls import path
from .views import JDCreateView, MatchResumeView

urlpatterns = [
    path('create/', JDCreateView.as_view()),
    path('match/', MatchResumeView.as_view()),
]
