from django import forms

class ContactoForm(forms.Form):
    nombre=forms.CharField(max_length=50,label='Nombre', required=True)
    apellido=forms.CharField(max_length=50,label='Apellido', required=True)
    email=forms.EmailField(max_length=50,label='Email', required=True)
    edad=forms.IntegerField(label='Edad',min_value=1,max_value=120, required=True)
    mensaje=forms.CharField(widget=forms.Textarea,label='Mensaje', required=True)
