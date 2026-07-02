from django.shortcuts import render

# Create your views here.
from .models import *
from .serializer import *

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def CategoryViews(request):
    Categories = Category.objects.all()
    serializer = CategorySerializer(Categories, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def featuredViews(request):

    featured = Blog.objects.filter(
        is_featured=True
    ).order_by('-created_at').first()

    if not featured:
        return Response({})

    serializer = BlogSerializer(
        featured,
        context={'request': request}
    )

    return Response(serializer.data)