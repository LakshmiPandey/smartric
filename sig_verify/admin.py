from django.contrib import admin

# Register your models here.
from django.contrib import admin

from sig_verify.models import register
admin.site.register(register)
