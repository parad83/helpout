from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.http import Http404
from . import forms

from . import models

def organisations(request):
    organisations = models.Organisation.objects.all()
    return render(request, 'organisation/organisations.html', {'organisations': organisations})
    
    
def organisation_details(request, slug):
    try:
        organisation = models.Organisation.objects.get(slug=slug)
    except ObjectDoesNotExist:
        raise Http404
    form = message.forms.MessageForm()
    
    context = {
        'organisation': organisation,
        'form': form,
    }
    
    if request.method == 'POST':
        form = message.forms.MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.receiver = organisation.user
            msg.save()
            return redirect(reverse('home'))
    return render(request, 'organisation/organisation_details.html', {'context': context})


def create_organisation(request):
    if request.user.can_have_organisation and not request.user.has_organisation:
        if request.method == 'POST':
            form = forms.OrganisationForm(request.POST, request.FILES)
            if form.is_valid():
                org = form.save(commit=False)
                org.user = request.user
                org.slug = slugify(org.name)
                org.save()
                request.user.has_organisation = True
                request.user.save()
                return redirect(reverse('organisations-view'))
        else:
            form = forms.OrganisationForm()        
        return render(request, 'create_organisation.html', {'form': form})
    else:
        return redirect(reverse('home'))
    
    
def edit_organisation(request):
    if request.user.has_organisation:
        organisation = get_object_or_404(models.Organisation, user=request.user)
        img = organisation.image
        if request.method == 'POST':
            form = forms.EditOrganisationForm(request.POST)
            organisation.name = form.data['name']
            organisation.biography = form.data['biography']
            organisation.website = form.data['website']
            organisation.slug = slugify(form.data['name'])
            organisation.save(update_fields=['name', 'biography', 'website', 'slug'])
        else:
            form = forms.EditOrganisationForm(
                data={
                    'name': organisation.name,
                    'biography': organisation.biography,
                    'website': organisation.website,
                },
            )
        return render(request, 'edit_organisation.html', {'form': form, 'img': img})
    else:
        return redirect(reverse('home'))
