from django.urls import path

from apps.collaborators.views import home

urlpatterns = [
    path('', home),
]
