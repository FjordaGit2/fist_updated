from django import forms

from .models import SignUp

class ContactForm(forms.Form):
	full_name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField(max_length = 12000,widget=forms.Textarea)

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name','email','institution']
		# exclude = ['full_name'] use sparingly

	def clean_email(self):
		email = self.cleaned_data.get('email')
		#email_base, provider = email.split("@")
		#domain, extension = provider.split(".")
		# if not domain == 'USC':
			# raise forms.ValidationError("please use USC email")
		# if not extension == "edu":
		# 	raise forms.ValidationError("Please use a valid college email address")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name
		


