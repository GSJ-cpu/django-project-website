from django.urls import path

from .views import SignUpView


urlpatterns = [
    path("signups/", SignUpView.as_view(), name="signups"),
]