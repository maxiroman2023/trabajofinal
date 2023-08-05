from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        exclude = ['created_at', 'is_read']
        labels = {
            'full_name': 'Nombre completo',
            'email_address': 'Correo electrónico',
            'message_body': 'Mensaje',
        }