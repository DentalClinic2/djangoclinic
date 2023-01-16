from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView

from . import views
from .forms import PwdResetConfirmForm, PwdResetForm, UserLoginForm

# https://docs.djangoproject.com/en/3.1/topics/auth/default/
# https://ccbv.co.uk/projects/Django/3.0/django.contrib.auth.views/PasswordResetConfirmView/

app_name = "accounts"







urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="account/login.html", form_class=UserLoginForm),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="/accounts/login/"), name="logout"),
    path("register/", views.account_register, name="register"),
    path("activate/<slug:uidb64>/<slug:token>)/", views.account_activate, name="activate"),
    # Reset password
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="account/password_reset/password_reset_form.html",
            success_url="password_reset_email_confirm",
            email_template_name="account/password_reset/password_reset_email.html",
            form_class=PwdResetForm,
        ),
        name="pwdreset",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="account/password_reset/password_reset_confirm.html",
            success_url="password_reset_complete/",
            form_class=PwdResetConfirmForm,
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset/password_reset_email_confirm/",
        TemplateView.as_view(template_name="account/password_reset/reset_status.html"),
        name="password_reset_done",
    ),
    # path(
    #     "password_reset_confirm/Mg/password_reset_complete/",
    #     TemplateView.as_view(template_name="account/password_reset/reset_status.html"),
    #     name="password_reset_complete",
    # ),
    path("password_reset_confirm/Ng/password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(
            template_name="account/password_reset/password_reset_complete.html",
    ), name='password_reset_complete'),
        path("profile/deactivate_user/", views.deactivate_user, name="deactivate_user"),
    path(
        "profile/deactivate_confirm/",
        TemplateView.as_view(template_name="account/dashboard/deactivate_confirm.html"),
        name="deactivate_confirmation",
    ),
    # User dashboard
    path("profile/edit/", views.edit_details, name="edit_details"),
    path("profile/show/", views.show_details, name="show_details"),


]