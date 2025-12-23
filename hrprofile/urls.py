from django.urls import path
from .views import HRProfileView

urlpatterns = [
    path("profile/", HRProfileView.as_view())
]
