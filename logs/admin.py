from django.contrib import admin
from .models import Log, UserLog, TestRecord

# Register your models here.
admin.site.register(Log)
admin.site.register(UserLog)
admin.site.register(TestRecord)