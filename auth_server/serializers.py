'''
Created on Jul 16, 2014

@author: hieunguyen
'''
from rest_framework import serializers
from auth_server.models import User, Client, AccessToken

class TokenSerializer(serializers.ModelSerializer):    
    class Meta:
        model = AccessToken
        fields = ('user', 'access_token', 'refresh_token')