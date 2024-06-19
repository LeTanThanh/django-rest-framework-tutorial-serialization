from django.urls import path

from .views import list_snippets

urlpatterns = [
    path('snippets/', list_snippets)
]
