from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import CommitteeOfficer
import json

# Create your views here.

def index(response):
    return HttpResponse("Hi ITC!")

def officers(request):
    if request.method == "GET":     
        data = list(CommitteeOfficer.objects.values('id','name','year','hobby'))
        return JsonResponse(data, safe=False, status = 200)
    elif request.method == "POST":
        new_data = json.loads(request.body)
        data.append(new_data)
        return JsonResponse(data, status = 200)

def officers_detail(request, num):
    data = list(CommitteeOfficer.objects.values('id','name','year','hobby'))
    try:
        new_data = next(new_data for new_data in data if new_data["id"] == num)
    except StopIteration:
        return JsonResponse({"status": f"There is no data for the id {num}"})

    if request.method == "GET": 
        return JsonResponse(new_data)
    elif request.method == "DELETE":
        data = list(filter(lambda new_data: new_data["id"] != num, data))
        return HttpResponse(status=204)