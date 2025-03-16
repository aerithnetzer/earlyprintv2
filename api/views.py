from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def api_index(request):
    data = {"name": "EarlyPrintV2 API", "version": "0.0.1"}
    return JsonResponse(data)
