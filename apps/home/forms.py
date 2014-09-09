from django import forms 

class LoginForm(forms.Form):
	username    = forms.CharField(widget=forms.TextInput()) 
	password    = forms.CharField(widget=forms.PasswordInput(render_value=False))
	
class sugerencias(forms.Form):
	Titulo      = forms.CharField(widget=forms.TextInput())
	sugerencia  = forms.CharField(widget=forms.Textarea())


