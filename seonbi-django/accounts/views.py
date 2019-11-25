from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, get_user
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializers

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    if request.method == 'POST':
        serializers = UserSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data)
    return Response({})

@api_view(['GET'])
@permission_classes([AllowAny])
def index(request):
    User = get_user_model()
    users = User.objects.all()
    serializers = UserSerializers(users, many=True)
    return Response(serializers.data)