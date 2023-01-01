from cProfile import label
from dataclasses import field
from decimal import DefaultContext
from email.policy import default
from operator import attrgetter
from secrets import choice
from . import models, urls
from django import forms
from django.core.exceptions import ObjectDoesNotExist

class DateInput(forms.DateInput):
    input_type = 'date'

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = [
            'title',
            'text',
            'image',
            'category',
            'area',
            'type',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control p-2',
            }),
            'category': forms.Select(attrs={
                'class': 'form-select p-2',
                
            }),
            'text': forms.Textarea(attrs={
                'rows': 8,
                'class': 'form-control p-2',
            }),
            'area': forms.TextInput(attrs={
                'class': 'form-control p-2',
                'name': 'area',
                'id': 'area',
                'onfocus': "this.value=''"
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control p-2',
                'id': 'image',
            }),
            'type': forms.RadioSelect(attrs={
                'class': 'form-check-input',
            }),
        }
        error_messages = {
            'title': {
                'required': ("Oops, You forgot to enter the title!"),
            },
            'text': {
                'required': ("Oops, You forgot to enter the description!"),
            },
            'area': {
                'required': ("Oops, You forgot to enter the area!"),
            },
            'category': {
                'required': ("Oops, You forgot to choose the category!"),
            },
            'type': {
                'required': ("Oops, You forgot about something!"),
            },
        }
        
class EditPostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = [
            'text',
            'image',
        ]
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 8,
                'class': 'form-control p-2',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control p-2',
                'id': 'image',
            }),
        }
        error_messages = {
            'text': {
                'required': ("Oops, You forgot to enter the description!"),
            },
        }
        
class CategoryForm(forms.ModelForm): 
    class Meta:
        model = models.Category
        fields = ('name',)
        
    name = forms.ModelMultipleChoiceField(
        queryset=models.Category.objects.all(), 
        # to_field_name='name', 
        label=False,
        widget=forms.Select(
            attrs={
                'class': 'sort-posts-form p-2 ps-0 pb-1',
                'id': 'category-input'
    }))

 
SORT_CHOICES = (
     ('relevance', 'Relevance'),
     ('newest', 'Newest'),
     ('oldest' , 'Oldest')
 )       
        
class SortForm(forms.Form):
    sort = forms.CharField(
        label=False,
        widget=forms.Select(choices=SORT_CHOICES, attrs={
            'class': 'sort-posts-form p-2 ps-0 pb-1',
            'id': 'sort-input'
    }))
    
    
DEFAULT = '...'
LOOKING_FOR_HELP = "...looking for help"
OFFERING_HELP = "...offering help"

POST_TYPES = (
    ("", DEFAULT),
    ("need", LOOKING_FOR_HELP),
    ("offer", OFFERING_HELP),
)
    
class TypeForm(forms.Form):
    type = forms.CharField(
        label=False,
        widget=forms.Select(
            choices=POST_TYPES,
            attrs={
                'class': 'sort-posts-form p-2',
                'id': 'type-input',
    }))