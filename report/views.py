from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
import account, post
from . import models
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def updateUserRating(user_id):
    user = get_object_or_404(get_user_model(), id=user_id)
    if int(user.rating) > 1:
        user.rating -= 1
        user.save(update_fields=['rating'])
    else:
        user.can_create_posts = False
        user.can_report = False
        user.save(update_fields=['can_create_posts', 'can_report', 'can_send_messages'])
        
        posts = models.Post.objects.filter(author=user)
        for p in posts:
            p.visible = False
            p.save(update_fields=['visible'])
            
def updatePostRating(post_id):
    p = get_object_or_404(post.models.Post, id=post_id)
    if int(p.rating) > 1:
        p.rating -= 1
        p.save(update_fields=['rating'])
    else:
        p.visible = False
        p.save(update_fields=['visible'])
    updateUserRating(p.author.id)
    
@login_required()
def report_post(request, post_id):
    if request.user.can_report:
        if not models.ReportPost.objects.filter(author=request.user, post=post_id):
            p = get_object_or_404(post.models.Post, id=post_id)
            report = models.ReportPost(
                author = request.user,
                post = p
            )
            report.save()
            updatePostRating(post_id)
            messages.add_message(request, messages.INFO, 'Post with ID: {} has been reported'.format(post_id))
        else:
            messages.add_message(request, messages.INFO, "You've already reported that post 😬")
    return redirect(reverse('posts'))