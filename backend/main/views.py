from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import CommitteeOfficer
import json

# Create your views here.

def index(response):

    return HttpResponse("shh")

def officers(request):
    if request.method == "GET":     
        data = list(CommitteeOfficer.objects.values('id','name','year','hobby'))
        return JsonResponse(data, safe=False, status = 200)
    elif request.method == "POST":
        new_data = json.loads(request.body)
        print(new_data)

def officers_detail():
    return 0