"""
URL configuration for earlyprintv2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.db.models import indexes
from django.urls import path
from earlyprint.views import (
    load_xml_to_db,
    list_json_objects,
    view_json_object,
    index,
    search_results,
)
from api.views import api_index, api_search

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("load-xml/", load_xml_to_db, name="load_xml_to_db"),
    path("json-objects/", list_json_objects, name="list_json_objects"),
    path("json-objects/<int:pk>/", view_json_object, name="view_json_object"),
    path(
        "api/",
        api_index,
        name="api_index",
    ),
    path("api/search/", api_search, name="api_search"),
    path("search-results/", search_results, name="search_results"),
]
