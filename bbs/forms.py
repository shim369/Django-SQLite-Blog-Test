from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(label='Subject', max_length=100)
	sender = forms.EmailField(label='E-mail')
	message = forms.CharField(label='Message', widget=forms.Textarea)
	myself = forms.BooleanField(label='Receive the same', required=False)