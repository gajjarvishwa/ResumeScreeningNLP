from django.urls import path
from .views import HRSignupView, LoginView

urlpatterns = [
    path("signup/", HRSignupView.as_view()),
    path("login/", LoginView.as_view()),   # VERY IMPORTANT
]
