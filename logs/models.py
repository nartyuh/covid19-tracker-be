from django.db import models
from users.models import User
import uuid

# Create your models here.


class Log(models.Model):
    id  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    latitude = models.DecimalField(max_digits=20, decimal_places=17)
    longitude = models.DecimalField(max_digits=20, decimal_places=17)
    log_start = models.DateTimeField(null=False, blank=False)
    log_end = models.DateTimeField(null=False, blank=False)

    class Meta:
        unique_together = ('latitude', 'longitude', 'log_start', 'log_end',)


class UserLog(models.Model):
    user = models.ForeignKey(User, to_field='username', null=False, blank=False, on_delete=models.CASCADE)
    log = models.ForeignKey(Log, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'log',)


class TestPositive(models.Model):
    user = models.ForeignKey(User, to_field='username', null=False, blank=False, on_delete=models.CASCADE)
    date_tested = models.DateField(null=False, blank=False)

    class Meta:
        unique_together = ('user', 'date_tested',)