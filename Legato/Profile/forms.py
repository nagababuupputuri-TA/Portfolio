from django import forms
from .models import Contact_model_form,Deployed_data,Text_speech_model
class contact_form(forms.ModelForm):
    class Meta:
        model=Contact_model_form
        fields=["full_name","email","subject","message"]
        labels=[("full_name,FullName"),("email","Email"),("subject","Subject"),("message","Message")]

class Deploy_form(forms.ModelForm):
    class Meta:
        model=Deployed_data
        fields='__all__'

## create a form for Text to speech

class Text_to_speech_from(forms.ModelForm):
    text=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter text '}))
    class Meta:
        model=Text_speech_model
        fields=['text']



