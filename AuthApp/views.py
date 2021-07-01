from django.contrib.auth.views import LoginView as CoreLoginView
from django.contrib.auth.views import LogoutView as CoreLogoutView
from django.contrib.auth import login

from django.urls import reverse
from django.views.generic.edit import FormView
from .forms import UserCreationForm

class LoginView(CoreLoginView):
	template_name='AuthApp/login_user.html'

class LogoutView(CoreLogoutView):
	template_name='AuthApp/logout_user.html'

class RegisterView(FormView):
	template_name = 'AuthApp/register_user.html'
	form_class = UserCreationForm

	def form_valid(self,form):
		user = form.save()
		return super().form_valid(form)
	
	def get_success_url(self):
		return reverse('register-success');