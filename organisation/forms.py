from . import models
from django import forms

class OrganisationForm(forms.ModelForm):
    
    class Meta:
        model = models.Organisation
        fields = (
            'name',
            'image',
            'biography',
            'website',
        )
        widgets = {
            # 'website':forms.URLField(
            #     attrs={
            #         'class':''
            #     }
            # ),
            'biography': forms.Textarea(
                attrs={
                    "rows": 4,
                }
            )
        }
        
class EditOrganisationForm(forms.ModelForm):
    
    class Meta:
        model = models.Organisation
        fields = (
            'name',
            'biography',
            'website',
        )
        exclude = {
            'image',
        }
        widgets = {
            # 'website':forms.URLField(
            #     attrs={
            #         'class':''
            #     }
            # ),
            'biography': forms.Textarea(
                attrs={
                    "rows": 4,
                }
            )
        }