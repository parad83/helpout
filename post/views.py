from unicodedata import category
from django.forms import IntegerField, ValidationError
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from requests import post
from . import models, forms
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
import shortuuid
from django.urls import reverse
from ia import settings
from django.db.models import Q 
from django.contrib.auth import get_user_model
from account.models import profanity_filter
from django.db import IntegrityError
from django.forms import ValidationError
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Count
from django.contrib import messages

def idExists(id):
    try:
        post = models.Post.objects.get(id=id)
    except ObjectDoesNotExist:
        return id
    return idExists(shortuuid.ShortUUID().random(length=10))

def home_view(request):
    look_for_help_posts = models.Post.objects.filter(type='need').order_by('-rating')[:4]
    offer_help_posts = models.Post.objects.filter(type='offer').order_by('-rating')[:4]
    categories = models.Category.objects.all()
    return render(request, 'home.html', {'look_for_help_posts': look_for_help_posts, 'offer_help_posts': offer_help_posts, 'categories': categories})


def posts(request, category=''):
    search = request.GET.get('search')
    sort = request.GET.get('sort')
    area=request.GET.get('area')
    type=request.GET.get('type')
    
    sort_by = 'rating'
    posts = models.Post.objects.all()
    
    if sort and sort !='':
        if sort == 'newest':
            sort_by = '-date_created'
        elif sort == 'oldest':
            sort_by = 'date_created'
            
    if 'search' in request.GET and search != '':
        posts = posts.filter(title__icontains=search)
    if 'area' in request.GET and area != '':
        posts = posts.filter(area__icontains=area)
    if category and category != '':
        posts = posts.filter(category__name=category)
    if 'type' in request.GET and type != '':
        posts = posts.filter(type=type)
        
    posts = posts.order_by(sort_by)
    
    sort_form = forms.SortForm(initial={'sort': sort})
    type_form = forms.TypeForm(initial={'type': type})
    
    paginator = Paginator(posts, 50)
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)
    
    categories = models.Category.objects.annotate(
            posts_count=Count('post')
        ).order_by('-posts_count')
    
    post_count = posts.count()
    
    context = {
        'posts': page_obj,
        'sort_form': sort_form,
        'type_form': type_form,
        'categories': categories,
        'post_count': post_count
    }
    return render(request, 'search_posts.html', {'context': context})


@login_required()
def create_post(request):
    if request.user.can_create_posts:
        if request.method == 'POST':
            form = forms.CreatePostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.id = idExists(shortuuid.ShortUUID().random(length=10))
                post.save()
                messages.add_message(request, messages.INFO, 'Post has been created.')
                return redirect(reverse('posts'))
        else:
            form = forms.CreatePostForm()
        return render(request, 'create_post.html', {'form': form})
    return redirect(reverse('home'))


def post_details(request, id):
    post = get_object_or_404(models.Post, id=id)
    posts = models.Post.objects.filter(author=post.author).order_by('-date_created')[:5]
    
    context = {
        'post': post,
        'authors_posts': posts
    }
    
    return render(request, 'post_details.html', {'context': context})

@login_required()
def edit_post(request, id):
    post = get_object_or_404(models.Post, id=id)
    if request.user == post.author:
        img = post.image
        if request.method == 'POST':
            form = forms.EditPostForm(request.POST, request.FILES)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.author = request.user
                new_post.id = idExists(shortuuid.ShortUUID().random(length=10))
                new_post.title = post.title
                new_post.area = post.area
                new_post.type = post.type
                new_post.category = post.category
                post.delete()
                new_post.save()
                messages.add_message(request, messages.INFO, 'Post has been updated.')
                return redirect(reverse('posts'))
        else:
            form = forms.EditPostForm(
                initial={
                    'title': post.title,
                    'text': post.text,
                    'category': post.category,
                    'type': post.type,
                },
            )
        context = {
            'form': form,
            'post': post,
            'img': img
        }
        return render(request, 'edit_post.html', {'context': context})

@login_required()
def delete_post(request, id):
    post = get_object_or_404(models.Post, id=id)
    if request.user == post.author:
        post.delete()
        messages.add_message(request, messages.INFO, 'Post has been deleted.')
    return redirect(reverse('account-view', args=[request.user.id]))
