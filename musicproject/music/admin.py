from django.contrib import admin
from django.contrib.auth.models import User
from music.models import music,category,event,message,CustomUser
# Register your models here.

admin.site.register(music)
admin.site.register(category)
admin.site.register(event)
admin.site.register(message)
admin.site.register(CustomUser)