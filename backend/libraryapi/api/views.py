from .models import Book,CustomUser
from rest_framework import viewsets,status
from .serializers import BookSerializer,UserSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.views import Token

from .customPermission import isAdmin

class BookAdminViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # using custom permision class and onl allowing users with usertype = 1 
    permission_classes = [isAdmin]
    # using token based authenctication system. 
    authentication_classes = [TokenAuthentication]

class BookStudentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    
    # creating custom token obtaining class as simple class only return token for a user 
    # after successsful login ,
    #  while i wanted its userid as well as it usertype with it
class Custom_auth_token(ObtainAuthToken):
    def post(self , req , *args , **kwargs):
        serializer = self.serializer_class(data = req.data , context = {'request' : req})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token , created = Token.objects.get_or_create(user = user)
        return Response({"token" : token.key,
        'user_id' : user.pk , 
        'UserType' : user.UserType} , status=status.HTTP_200_OK)




