from django.db import models

class register(models.Model):
    ACCOUNT_NUMBER = models.IntegerField()
    SIGNATURE_URLS = models.CharField(max_length=256)
    picture = models.ImageField(upload_to = 'Signatures/')
