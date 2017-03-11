from datetime import datetime
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import UserSerializer


class UserView(RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class ObtainJsonWebToken(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request, *args, **kwargs):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

        user = request.user
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        response_data = jwt_response_payload_handler(token, user, request)

        response = Response(response_data)

        # if api_settings.JWT_AUTH_COOKIE:
        #     expiration = (datetime.utcnow() +
        #                   api_settings.JWT_EXPIRATION_DELTA)
        #     response.set_cookie(api_settings.JWT_AUTH_COOKIE,
        #                         response.data['token'],
        #                         expires=expiration,
        #                         httponly=True)
        return response
