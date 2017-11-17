from django.db import models
from django.utils import timezone

class License(models.Model):
#    license_type = models.ForeignKey('license_type.Type')
    type = models.TextField(blank=True, null=True)
    consumed_by = models.ForeignKey('auth.User', blank=True, null=True)
    body = models.TextField()
    tags = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)
    expiry = models.DateTimeField(
            blank=True, null=True)

    def consume(self):
        self.published_date = timezone.now()
        self.save()

    def unconsume(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.body
