from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
	path('login/', views.LoginView.as_view(), name="login"),
	path('logout/', views.LogoutView.as_view(), name="logout"),
	path('register/', views.RegisterView.as_view(), name="register"),
	path('register_success', TemplateView.as_view(template_name="AuthApp/register_success.html"), name="register-success")
]