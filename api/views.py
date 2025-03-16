from django.shortcuts import render
from django.http import JsonResponse
from earlyprint.models import Work
# Create your views here.


def api_index(request):
    data = {"name": "EarlyPrintV2 API", "version": "0.0.1"}
    return JsonResponse(data)


def api_search(request):
    query = request.GET.get("query")
    if query:
        results = Work.objects.filter(json_data__icontains=query)
        # Create a list of dictionaries with work and title
        # JSONify the results
        results = [result.json_data for result in results]
        # Return the results as JSON
        return JsonResponse(results, safe=False)
