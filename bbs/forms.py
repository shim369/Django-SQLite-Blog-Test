from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100,
            widget=forms.TextInput(
            attrs={'placeholder':'Subject', 'class':'contact-input'}))
	sender = forms.EmailField(widget=forms.TextInput(
            attrs={'placeholder':'E-mail', 'class':'contact-input'}))
	message = forms.CharField(widget=forms.Textarea(
            attrs={'placeholder':'Message', 'class':'contact-input'}))
	myself = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'id':'box'}))

class BmiForm(forms.Form):
	height = forms.IntegerField(widget=forms.NumberInput(
            attrs={'min':'1', 'class':'bmi-input'}))
	weight = forms.IntegerField(widget=forms.NumberInput(
            attrs={'min':'1', 'class':'bmi-input'}))