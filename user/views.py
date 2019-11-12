from django.http import HttpResponse
# from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from .serializers import LoginSerializer, RegisterSerializer
from rest_framework.decorators import api_view,permission_classes,authentication_classes

# Create your views here.

def welcome(request):
    return HttpResponse("<center><h3>Welcome to Superman.</h3></center>")

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)  
    user = serializer.save()
    data = {}
    data['status'] = 'success'
    data['message'] = 'Successfully Registration.'
    data['email'] = user.email
    return Response(data)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login(request,format=None):

    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    token = serializer.validated_data["token"]

    return Response({
        'token': token,
        'status': 'success',
        'message': 'Successfully Login.'
        })