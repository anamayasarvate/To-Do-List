from django import forms
from .models import ToDo

class CreateForm(forms.ModelForm):
	item = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Write your task'}))
	class Meta():
		model = ToDo
		fields = ["item"]
