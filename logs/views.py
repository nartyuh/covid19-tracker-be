from django.shortcuts import render, HttpResponse

import uuid

from rest_framework import generics, permissions, status, HTTP_HEADER_ENCODING
from rest_framework.response import Response

from knox.models import AuthToken

from .serializer import LogSerializer, UserLogSerializer, TestPositiveSerializer
from .models import Log, UserLog, TestPositive

from users.auth import TokenAuthentication


# Create your views here.


class LogAPI(generics.GenericAPIView):

    queryset = Log.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = LogSerializer

    def get(self, request, format=None):
        user_id = request.user.username
        user_logs = UserLog.objects.filter(user=user_id)

        logs = []
        for user_log in user_logs:
            log = user_log.log
            logs.append(log)
        
        serializer = LogSerializer(logs, many=True)

        return Response(serializer.data)

    def post(self, request):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        log = serializer.save()
        user_log = UserLog(user=user, log=log)
        user_log.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class TestPositiveApi(generics.GenericAPIView):

    queryset = TestPositive.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TestPositiveSerializer

    def get(self, request, format=None):
        user =""
        # user = request.user
        try:
            test_positive = TestPositive.objects.get(user=user)
        except:
            return Response(None, status=status.HTTP_204_NO_CONTENT)

        serializer = TestPositiveSerializer(test_positive)

        return Response(serializer.data)

    def post(self, request):
        user = request.user
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # test_positive = serializer.save()
        test_positive = TestPositive(user=user, date_tested=request.data['date_tested'])
        test_positive.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)