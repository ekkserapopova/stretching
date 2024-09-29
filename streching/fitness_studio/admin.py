from django.contrib import admin
from .models import Filial, Schedule, CustomUser, Activities, Record

# Register your models here.
admin.site.register(Filial)
admin.site.register(Schedule)
admin.site.register(CustomUser)
admin.site.register(Activities)
admin.site.register(Record)
