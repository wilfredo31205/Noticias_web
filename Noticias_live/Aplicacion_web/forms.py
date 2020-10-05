from django import forms

class FormularioContacto(forms.Form):

    asunto=forms.CharField()
    Email=forms.EmailField()
    mensaje=forms.CharField(widget=forms.Textarea)

 