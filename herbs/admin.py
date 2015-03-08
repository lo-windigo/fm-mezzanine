from __future__ import unicode_literals

from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from models import HerbGallery, Herb


class HerbImageInline(TabularDynamicInlineAdmin):
    model = Herb


class HerbGalleryAdmin(PageAdmin):

    class Media:
        css = {"all": ("mezzanine/css/admin/gallery.css",)}

    inlines = (HerbImageInline,)


admin.site.register(HerbGallery, HerbGalleryAdmin)
