from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import HerbsGallery


admin.site.register(HerbsGallery, PageAdmin)
