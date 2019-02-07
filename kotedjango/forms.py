from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()
class ContactForm(forms.Form):
	fullname = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "id":"form_full_name", "placeholder":"Your Full Name"}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder":"Your email"}))
	content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder":"Your message"}))

	def clean_email(self):
		email = self.cleaned_data.get("email")
		if not "gmail.com" in email:
			raise forms.ValidationError("Email has to be gmail.com")
		return email		

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Your Login"}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))		
class RegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Your Login"}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder":"Your email"}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))	
	password_conf = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={"class":"form-control"}))	
	def clean_username(self):
		username = self.cleaned_data.get("username")
		qs=User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("This username already taken, choose another one")
		return username	
	def clean_email(self):
		email = self.cleaned_data.get("email")
		qs=User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("This email already taken, enter another one")
		return email			
	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get("password")
		password_conf = self.cleaned_data.get("password_conf")
		if password_conf!=password :
			raise forms.ValidationError("Passwords must match")
		return data	