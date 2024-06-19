from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from snippets_app.models import Snippet
from snippets_app.serializers import SnippetSerializer


"""
Note that because we want to be able to POST to this view from clients that won't have CSRF token we neef to mark the view as csrf_exempt.
This isn't something that you'd normally want to do, and REST framework views actually use more sensible behavior than this, but it'll do for our purpose right now.

We'll also need a view which corresponds to an individual snippet, and can be used to retrieve, update or delete the snippet.
"""
@csrf_exempt
def snippets(request):
    if request.method == "GET":
        return list_snippets(request=request)
    elif request.method == "POST":
        return create_snippet(request=request)


def list_snippets(request):
    snippets = Snippet.objects.all()
    serializer = SnippetSerializer(instance=snippets, many=True)
    return JsonResponse(data=serializer.data, safe=False, status=200)


def create_snippet(request):
    data = JSONParser().parse(request)
    serializer = SnippetSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(data=serializer.data, status=201)

    return JsonResponse(data=serializer.errors, status=422)
