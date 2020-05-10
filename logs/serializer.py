from rest_framework import serializers
from .models import Log, UserLog, TestRecord



class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Log
        fields = ['id', 'latitude', 'longitude', 'log_start', 'log_end', 'time_zone']

        def create(self, validated_data):
            """
                create and return a log
            """
            return Log.objects.create(**validated_data)

        

# class UserLogSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = UserLog
#         fields = ['user', 'log']

#     def create(self, validated_data):
#         """
#             create and return a user log
#         """
#         return UserLog.objects.create(**validated_data)


class TestRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestRecord
        fields = ['date_tested', 'positive']