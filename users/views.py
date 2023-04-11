from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status
from users.models import User
from .serializers import UserSerializer
# Create your views here.


class UserView(APIView):
    def get(self, request: Request) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)