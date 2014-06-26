from django.contrib import admin
from herbs.models import Herb, HerbGallery
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin


class HerbInline(TabularDynamicInlineAdmin):
	model = Herb


class HerbAdmin(PageAdmin):
	inlines = (HerbInline,)

#admin.site.register(Herb, PageAdmin)
admin.site.register(HerbGallery, HerbAdmin)
