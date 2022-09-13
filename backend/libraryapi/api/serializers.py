from rest_framework.authtoken.views import Token
from .models import Book,CustomUser
from rest_framework import serializers

from django.contrib.auth import get_user_model
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as JwtTokenObtainPairSerializer


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields  = ['id','Name','Author','Discription']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','email', 'password')

        extra_kwargs = {'password':{ 'write_only':True,'required':True }}
        # making password write only as we do not want to send it to frontend after user is created


    def create(self, validated_data):
        user = get_user_model().objects.create(**validated_data)
        print(validated_data['password'])
        user.set_password(validated_data['password'])
        Token.objects.create(user=user)
        # Generating token at the time of creating new user.(here user has usertpe = 2 ,ie student)
        user.save()
        return user

    