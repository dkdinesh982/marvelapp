from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,serializers,parsers
from rest_framework.response import Response
from .models import *
from django.utils.timezone import now, timedelta
from oauth2_provider.settings import oauth2_settings
from oauthlib.common import generate_token
from oauth2_provider.models import AccessToken, Application, RefreshToken
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings    
from django.contrib.auth import get_user_model
import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

      

class registerViewSet(viewsets.ViewSet):
        # permission_classes = [TokenHasReadWriteScope]
    def list(self, request):
        
        User_data = MyUser.objects.all()
        User_data_list = []
        for user in User_data:
            User_data_list.append({
                "id":user.id,
                "email":user.email,
                "name":user.name,
                "password":user.password,
                "mobile_number":user.mobile,
                'id_no':user.id_no,
                'account_type':user.account_type
                
                
            })
        return Response({"users":User_data_list})
    

    def create(self, request):
        id_no=request.data.get('id_no')
        account_type=request.data.get('account_type')
        name =request.data.get('name')
        email = request.data.get('email')
        
        password=request.data.get('password') 
        mobile_number=request.data.get('mobile')     
        
        user = MyUser()
        user.id_no=id_no
        user.account_type=account_type
        user.name = name
        user.email = email
        user.mobile=mobile_number
        user.set_password(password)

       
        user.save()

        app = Application.objects.create(user=user)
        token = generate_token()
        refresh_token = generate_token()
        expires = now() + timedelta(seconds=oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS)
        scope = "read write"
        access_token = AccessToken.objects.create(user=user,
                                            application=app,
                                            expires=expires,
                                            token=token,
                                            scope=scope,
                                            )
        print("access token ------->", access_token)
        RefreshToken.objects.create(user=user,
                                    application=app,
                                    token=refresh_token,
                                    access_token=access_token
                                    )
        response = {
            'access_token': access_token.token,
            'expires_in': oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS,
            'token_type': 'Bearer',
            'refresh_token': access_token.refresh_token.token,
            'client_id': app.client_id,
            'client_secret': app.client_secret
            }
       
       
        return Response({"response":response})

class LoginViewSet(viewsets.ViewSet):
   def create(self, request): 
        email = request.data.get('email')
        password=request.data.get('password')  
        user = authenticate(email=email, password=password)
        
        if user is not None:
            app = Application.objects.get(user=user)  
            token = generate_token()
            refresh_token = generate_token()
            expires = now() + timedelta(seconds=oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS)
            scope = "read write"
            access_token = AccessToken.objects.create(user=user,
                                                    application=app,
                                                    expires=expires,
                                                    token=token,
                                                    scope=scope,
                                                    )
            
            RefreshToken.objects.create(user=user,
                                    application=app,
                                    token=refresh_token,
                                    access_token=access_token
                                    )
            response = {
                'access_token': access_token.token,
                'expires_in': oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS,
                'token_type': 'Bearer',
                'refresh_token': access_token.refresh_token.token,
                'client_id': app.client_id,
                'client_secret': app.client_secret
            }
        
            return Response({"response":response}) 
        
        else:
        
            return Response("excess denied")   


