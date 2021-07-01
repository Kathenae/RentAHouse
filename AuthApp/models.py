from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

	def create_user(self,email,nome,sobrenome,password=None):
		new_user = User(email=email,nome=nome,sobrenome=sobrenome)
		new_user.set_password(password)
		new_user.is_active = True
		new_user.save()
		return new_user

	def create_superuser(self, email,nome,sobrenome,password=None):
		new_user = self.create_user(email,nome,sobrenome,password)
		new_user.is_admin = True
		new_user.is_superuser = True
		new_user.save()
		return new_user

class User(PermissionsMixin,AbstractBaseUser):

	# Fields
	email = models.EmailField(unique=True,max_length=255, verbose_name='email')
	nome = models.CharField(max_length=100)
	sobrenome = models.CharField(max_length=100)
	
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	# Define Manager
	objects = UserManager()

	# Setup for default django authentication
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['nome', 'sobrenome']

	@property
	def is_staff(self):
		return self.is_admin
	
	def get_full_name(self):
		return self.nome + ' ' + self.sobrenome

	def get_short_name(self):
		return self.nome

	def __str__(self):
		return self.email