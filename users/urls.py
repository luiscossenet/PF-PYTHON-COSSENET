from django.urls import path
from users import views

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
    # path("profile/", views.profile, name="Profile"),
    # path("logout/", views.logout_request, name="Logout"),
    # path("profile/", views.profile, name="Profile"),
    # path("edit_profile/", views.edit_profile, name="Edit_Profile"),
    # path("change_password/", views.change_password, name="Change_Password"),
    # path("delete_profile/", views.delete_profile, name="Delete_Profile"),
    # path("password_reset/", views.password_reset_request, name="Password_Reset"),
    # path("password_reset/done/", views.password_reset_done, name="Password_Reset_Done"),
    # path("password_reset_confirm/<uidb64>/<token>/", views.password_reset_confirm, name="Password_Reset_Confirm"),
    # path("password_reset_complete/", views.password_reset_complete, name="Password_Reset_Complete"),
    # path("password_change/", views.password_change, name="Password_Change"),
    # path("password_change_done/", views.password_change_done, name="Password_Change_Done"),
    # path("password_change_form/", views.password_change_form, name="Password_Change_Form"),
]
