from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name="login-user"),
    path('logout', views.logout_user, name="logout-user"),


]
