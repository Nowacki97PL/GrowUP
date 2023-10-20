from django.urls import path

from accounts.views import SubmittableLoginView, Logout

app_name = 'accounts'

urlpatterns = [
    path("login/", SubmittableLoginView.as_view(template_name="registration/login.html"), name="login"),
    path("accounts/logout/", Logout.as_view(), name="logout"),
]