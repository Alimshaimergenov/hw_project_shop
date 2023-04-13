from django.shortcuts import HttpResponse
import datetime

def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project")

def nowdate_view(request):
    if request.method == 'GET':
        return HttpResponse(datetime.date.today())

def goodby_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodby user!")