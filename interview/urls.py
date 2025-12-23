from django.urls import path
from .views import ScheduleInterviewView

urlpatterns = [
    path("schedule/", ScheduleInterviewView.as_view()),
]
