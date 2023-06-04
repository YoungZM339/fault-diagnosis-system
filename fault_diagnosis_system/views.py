from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello world!")
