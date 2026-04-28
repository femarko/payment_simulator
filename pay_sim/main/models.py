from django.db import models


class Payment(models.Model):
    id = models.UUIDField(primary_key=True)
    status = models.CharField(max_length=20)
