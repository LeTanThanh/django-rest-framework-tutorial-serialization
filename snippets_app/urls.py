from django.urls import path

from .views import snippets
from .views import snippet

urlpatterns = [
    path('snippets/', snippets),
    path('snippets/<int:pk>/', snippet)
]
