from django.urls import path, include
from .views import LogAPI, TestRecordApi

urlpatterns = [
    path('', include('knox.urls')),
    path('log/', LogAPI.as_view()),
    path('teststatus/', TestRecordApi.as_view()),
]