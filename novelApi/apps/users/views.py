import random
import string
from datetime import datetime, timedelta

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.conf import settings
from rest_framework import mixins, viewsets, authentication, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from utils.sms import Sms
from utils.storage import Storage
from .models import VerifyCode
from .serializers import UserDetailSerializer, LoginSmsSerializer, RegSmsSerializer, UserRegSerialize

User = get_user_model()


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
            elif VerifyCode.objects.filter(mobile=username, code=password).exists():
                return user
        except Exception as e:
            return None


class LoginSmsCodeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = LoginSmsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data['mobile']
        code = ''.join(random.sample(string.digits, 6))
        api_key = settings.API_KEY
        sms = Sms(api_key)
        res = sms.send_sms(code=code, mobile=mobile)

        if res['code'] != 0:
            return Response({'non_field_errors': res['msg']}, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code, mobile=mobile)
            code_record.save()
            return Response({'mobile': mobile}, status=status.HTTP_201_CREATED)


class RegSmsCodeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = RegSmsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data['mobile']
        code = ''.join(random.sample(string.digits, 6))
        api_key = settings.API_KEY
        sms = Sms(api_key)
        res = sms.send_sms(code=code, mobile=mobile)

        if res['code'] != 0:
            return Response({'non_field_errors': res['msg']}, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code, mobile=mobile)
            code_record.save()
            return Response({'mobile': mobile}, status=status.HTTP_201_CREATED)


class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserDetailSerializer
        elif self.action == 'create':
            return UserRegSerialize
        return UserDetailSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated()]
        elif self.action == 'create':
            return []
        return []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        access_key = settings.AK
        secret_key = settings.SK
        bucket_name = settings.BUCKET
        storage = Storage(access_key, secret_key, bucket_name)
        upload_token = storage.get_upload_token()
        re_dict['upload_token'] = upload_token
        payload = jwt_payload_handler(user)
        re_dict['token'] = jwt_encode_handler(payload)
        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        re_dict = serializer.data
        access_key = settings.AK
        secret_key = settings.SK
        bucket_name = settings.BUCKET
        storage = Storage(access_key, secret_key, bucket_name)
        upload_token = storage.get_upload_token()
        re_dict['upload_token'] = upload_token
        return Response(re_dict)

    def get_object(self):
        return self.request.user
