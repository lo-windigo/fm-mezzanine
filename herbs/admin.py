from copy import deepcopy
from django.contrib import admin
from herbs.models import Herb, HerbGallery
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin


class HerbInline(TabularDynamicInlineAdmin):
	model = Herb
	prepopulated_fields = {
		"l_slug": ("latin",),
		"c_slug": ("common",),
	}


class HerbGalleryAdmin(PageAdmin):
	inlines = (HerbInline,)

#admin.site.register(Herb, PageAdmin)
admin.site.register(HerbGallery, HerbGalleryAdmin)
