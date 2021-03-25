from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, label='Nombre', max_length=50, min_length=2, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Escribe tu nombre'
        }
    ))
    email = forms.EmailField(required=True, label='Email', max_length=100, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Escribe tu email'
        }
    ))
    content = forms.CharField(required=True, label='Contenido', max_length=200, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Escribe tu mensaje...'
        }
    ))
