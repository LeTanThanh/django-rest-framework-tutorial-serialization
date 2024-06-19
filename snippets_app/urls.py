from django.urls import path

from .views import snippets

urlpatterns = [
    path('snippets/', snippets)
]
