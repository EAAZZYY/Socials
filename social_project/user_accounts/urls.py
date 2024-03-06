from django.urls import path
from . import views
from django.contrib.auth import views as django_views


urlpatterns = [
    # Profile Path
    path("index/",views.index,name="index"),
    path("profile/<int:id>/",views.profile,name='profile'),
    path('profile_edit/', views.profile_edit, name="profile_edit"),


    # Users Accounts
    path("register/",views.register,name='register'),
    path("login/",django_views.LoginView.as_view(template_name="user_accounts/login.html"),name='login'),
    path("logout/",django_views.LogoutView.as_view(template_name="user_accounts/logout.html"),name='logout'),
    
    
    # Password change url
    path("password_change/",django_views.PasswordChangeView.as_view(template_name="user_accounts/password_change.html"), name="password_change"),
    path("password_change/done/",django_views.PasswordChangeDoneView.as_view(template_name="user_accounts/password_change_done.html"), name="password_change_done"),
    
    # Password reset Url
    path("password_reset/",django_views.PasswordResetView.as_view(template_name="user_accounts/password_reset.html"),name="password_reset"),
    path("password_reset_done/",django_views.PasswordResetDoneView.as_view(template_name="user_accounts/password_reset_done.html"), name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>",django_views.PasswordResetConfirmView.as_view(template_name='user_accounts/password_reset_confirm.html'),name="password_reset_confirm"),
    path("password_reset_complete/",django_views.PasswordResetCompleteView.as_view(template_name="user_accounts/password_reset_complete.html"),name="password_reset_complete"),
    
]