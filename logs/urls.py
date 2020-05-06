from django.urls import path, include
from .views import LogAPI, TestPositiveApi, UpdateLogApi

urlpatterns = [
    path('', include('knox.urls')),
    path('log/', LogAPI.as_view()),
    path('update/', UpdateLogApi.as_view()),
    path('teststatus/', TestPositiveApi.as_view()),
]