from unicodedata import name
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
import json, requests
from django.utils.safestring import SafeString
import account, organisation, post, report
from post.models import PolandCities, Post, Category
from django.db.models import Q 
from django.http import JsonResponse


API_KEY = "AIzaSyDkmuX-Gn_voJSwSy6Y0WJHaBKLhzIvEbQ"

def test_api(request):
    print(account.models.User.objects.all())
    print(organisation.models.Organisation.objects.all())
    print(post.models.Category.objects.all())
    print(post.models.Post.objects.all())
    print(report.models.ReportUser.objects.all())
    print(report.models.ReportPost.objects.all())
    
    return render(request, 'api_test.html')

# def data_api(request):
#     if request.user.is_authenticated:
#         payload={}
#         headers = {}
        
#         q = request.GET.get('q')
        
#         url = "https://maps.googleapis.com/maps/api/place/autocomplete/json?input={}&types=(cities)&region=pl|ua&components=country:pl|country:ua&language=pl&key={}".format(q, API_KEY)
        
#         response = requests.request("GET", url, headers=headers, data=payload)
#         json_object = json.loads(response.text)
#         json_pretty = json.dumps(json_object, indent=4)
#         return HttpResponse(json_pretty, content_type='application/json')
#     return HttpResponse('', content_type='application/json')

def cities_api(request):
    q = request.GET.get('q')        # gets the input
    areas = list(PolandCities.objects.filter(name__istartswith=q).order_by('-population').values()[:5])     # filters through the database and returns first 5 values
    return JsonResponse(areas, safe=False, content_type='application/json')

def voiv_api(request):
    q = request.GET.get('q')
    areas = None
    if q:
        areas = list(PolandCities.objects.filter(voivodeship__istartswith=q).order_by('-population').values())
    return JsonResponse(areas, safe=False, content_type='application/json')

def categories_api(request):
    q = request.GET.get('q')
    posts = None
    if q:
        posts = list(Category.objects.filter(voivodeship__istartswith=q).values()[:5])
    return JsonResponse(posts, safe=False, content_type='application/json')