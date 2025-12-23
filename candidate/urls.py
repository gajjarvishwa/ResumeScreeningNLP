from django.urls import path
from .views import SaveAcceptedView, ListAcceptedView

urlpatterns = [
    path("save/", SaveAcceptedView.as_view()),
    path("list/", ListAcceptedView.as_view()),
]
