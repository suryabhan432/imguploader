from django.contrib import admin
from .models import Image


class ImageAdmin(admin.ModelAdmin):
	list_display = ['id','photo','date']
admin.site.register(Image,ImageAdmin)

