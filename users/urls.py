from django.urls import path
from users import views
from users.views import profile, edit_profile
from .views import CustomLogoutView

# from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("login/", views.login_request, name="Login"),
    path("register/", views.register, name="Register"),
    path(
        "logout/",
        CustomLogoutView.as_view(template_name="AppMagico/index.html"),
        name="Logout",
    ),
    path('profile/<str:username>/',  profile, name="RV_vProfile"),
    path("profileEdit/", edit_profile, name="RV_vEditProfile"),
]
