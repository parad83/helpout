from django import forms
from . import models

class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = (
            'email',
            'title',
            'text',
        )
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class':'form-control isd'
                },
            ),
            'text': forms.Textarea(
                attrs={
                    'class':'form-control phone'
                },
            ),    
        }
        error_messages = {
            'email': {
                'required': ("Email cannot be empty!"),
            },
            'text': {
                'required': ("Message cannot be empty!"),
            },
        }
            