from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Snippet
from .serializers import SnippetSerializer
from django.shortcuts import render, redirect
from django.http import HttpResponse
from PIL import Image
from rest_framework import serializers



@api_view(['GET'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response({"hey":"hey"})
