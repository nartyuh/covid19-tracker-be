from django.shortcuts import render, HttpResponse

import uuid
import time

from rest_framework import generics, permissions, status, HTTP_HEADER_ENCODING
from rest_framework.response import Response

from knox.models import AuthToken

from .serializer import LogSerializer, TestRecordSerializer
from .models import Log, UserLog, TestRecord

from users.auth import TokenAuthentication


# Create your views here.

class PreflightsOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == "OPTIONS"


class LogAPI(generics.GenericAPIView):

    queryset = Log.objects.all()
    permission_classes = [PreflightsOnly|permissions.IsAuthenticated]
    serializer_class = LogSerializer

    def get(self, request, format=None):
        try:
            user_id = request.user.username
            user_logs = UserLog.objects.filter(user=user_id)

            logs = []
            for user_log in user_logs:
                log = user_log.log
                logs.append(log)
            
            serializer = LogSerializer(logs, many=True)

            return Response(serializer.data)
        except:
            return Response(None, status=status.HTTP_502_BAD_GATEWAY)


    def post(self, request, format=None):
        try:
            user = request.user
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            log = serializer.save()
            user_log = UserLog(user=user, log=log)
            user_log.save()
            return Response({
                'status': 'Create log successfully'
            }, status=status.HTTP_200_OK)
        except:
            return Response(None, status=status.HTTP_502_BAD_GATEWAY)


    def put(self, request, format=None):
        try:
            request_data = request.data
            current_user = request.user
            user_with_log_id = UserLog.objects.get(log=request_data['id']).user
            if (current_user == user_with_log_id):
                log = Log.objects.get(id=request_data['id'])
                log.latitude = request_data['latitude']
                log.longitude = request_data['longitude']
                log.log_start = request_data['log_start']
                log.log_end = request_data['log_end']
                log.time_zone = request_data['time_zone']

                """
                sanity check
                """
                assert log.latitude == request_data['latitude']
                assert log.longitude == request_data['longitude']
                assert log.log_start == request_data['log_start']
                assert log.log_end == request_data['log_end']
                assert log.time_zone == request_data['time_zone']

                # save changes
                log.save()

                return Response({
                    'status': 'Update log successfully.'
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'status': 'Unauthorized'
                }, status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response(None, status=status.HTTP_502_BAD_GATEWAY)


    def delete(self, request, format=None):
        try:
            request_data = request.data
            current_user = request.user
            user_with_log_id = UserLog.objects.get(log=request_data['id']).user
            if (current_user == user_with_log_id):
                log = Log.objects.get(id=request_data['id'])

                # delete log
                log.delete()

                return Response({
                    'status': 'Delete log successfully.'
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'status': 'Unauthorized.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response(None, status=status.HTTP_502_BAD_GATEWAY)


class TestRecordApi(generics.GenericAPIView):

    queryset = TestRecord.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TestRecordSerializer

    def get(self, request, format=None):
        user = request.user
        try:
            test_record = TestRecord.objects.filter(user=user).latest('date_tested')
        except TestRecord.DoesNotExist:
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(None, status=status.HTTP_502_BAD_GATEWAY)

        serializer = TestRecordSerializer(test_record)

        return Response(serializer.data)

    def post(self, request):
        try:
            user = request.user
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            request_data = serializer.data
            test_record = TestRecord(user=user, date_tested=request_data['date_tested'], positive=request_data['positive'])
            test_record.save()
        except:
            return Response(None, status=status.HTTP_502_BAD_GATEWAY)
        return Response({
            'status': 'Update test status successfully.'
        }, status=status.HTTP_200_OK)