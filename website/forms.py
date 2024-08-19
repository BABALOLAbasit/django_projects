from django import forms 
from .models import Customer

class Customerform(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ['first_name', 'last_name', 'age', 'email', 'phone_number', 'password']