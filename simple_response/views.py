from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.
data = {
    "slackUsername":"Ocean", 
    "backend": True,
    "age":23,
    "bio": "programming is not actually what i thought it would be."
}


def json(request):
    return JsonResponse(data, safe = False)