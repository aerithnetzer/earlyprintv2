from django.shortcuts import render
from django.db.models import Q
import json
import requests
import xmltodict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from earlyprint.models import Work
from django.shortcuts import get_object_or_404


def index(request):
    return render(request, "earlyprint/index.html")


@csrf_exempt
def load_xml_to_db(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            xml_url = data.get("xml_url")
            if not xml_url:
                return JsonResponse({"error": "No XML URL provided"}, status=400)

            response = requests.get(xml_url)
            if response.status_code != 200:
                return JsonResponse({"error": "Failed to fetch XML"}, status=400)

            xml_data = response.content
            json_data = xmltodict.parse(xml_data)
            Work.objects.create(json_data=json_data)

            return JsonResponse({"message": "Data loaded successfully"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)


def list_json_objects(request):
    works = Work.objects.all()
    return render(request, "earlyprint/list_json_objects.html", {"works": works})


def view_json_object(request, pk):
    work = get_object_or_404(Work, pk=pk)
    pretty_json_data = json.dumps(work.json_data, indent=4)
    return render(
        request,
        "earlyprint/view_json_object.html",
        {"work": work, "pretty_json_data": pretty_json_data},
    )


def search_results(request):
    query = request.GET.get("query", "")
    author = request.GET.get("author", "")
    year = request.GET.get("year", "")
    publisher = request.GET.get("publisher", "")

    results = Work.objects.all()

    # Apply filters based on provided parameters
    if query:
        results = results.filter(json_data__icontains=query)

    # Filter by author if provided
    if author:
        results = results.filter(
            json_data__TEI__teiHeader__fileDesc__titleStmt__author__icontains=author
        )

    # Filter by year if provided
    if year:
        results = results.filter(
            json_data__TEI__teiHeader__fileDesc__publicationStmt__date__icontains=year
        )

    # Filter by publisher if provided
    if publisher:
        results = results.filter(
            json_data__TEI__teiHeader__fileDesc__publicationStmt__publisher__icontains=publisher
        )

    # Limit results to avoid overwhelming the page
    results = results[:10]

    # Create a list of dictionaries with work and title
    results_with_titles = []
    for result in results:
        title = (
            result.json_data.get("TEI", {})
            .get("teiHeader", {})
            .get("fileDesc", {})
            .get("titleStmt", {})
            .get("title", "No title available")
        )
        results_with_titles.append({"work": result, "title": title})

    return render(
        request, "earlyprint/search_results.html", {"results": results_with_titles}
    )
