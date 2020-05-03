from rest_framework import serializers
from .models import Log, UserLog, TestPositive



class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Log
        fields = ['id', 'latitude', 'longitude', 'log_start', 'log_end']

        def create(self, validated_data):
            """
                create and return a log
            """
            return Log.objects.create(**validated_data)

        

class UserLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserLog
        fields = ['user', 'log']

    def create(self, validated_data):
        """
            create and return a user log
        """
        return UserLog.objects.create(**validated_data)


class TestPositiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestPositive
        fields = ['user', 'date_tested']