from django.core.urlresolvers import reverse
from django.db import models
from mezzanine.core.models import Orderable
from mezzanine.pages.models import Page, RichText


class HerbGallery(Page):

	class Meta:
		verbose_name = u"Herb Gallery"
		verbose_name_plural = u"Herb Galleries"

	def can_add(self, request):
		return True

	def can_delete(self, request):
		return request.user.is_superuser #or self.parent is not None

	def can_move(self, request, new_parent):
		return True

#	def get_absolute_url(self):
#		return reverse("herb-gallery", args=[self.desc])


class Herb(Orderable):
	image   = models.ImageField("Picture", blank=True, upload_to="herbs/")
	common  = models.CharField("Herb", max_length=500)
	latin   = models.CharField('Botanical Name', max_length=500)
	price   = models.DecimalField('Dried Per Oz', max_digits=6, decimal_places=2)
	gallery = models.ForeignKey(HerbGallery, blank=True)

	class Meta:
		verbose_name = u"Herb"
		verbose_name_plural = u"Herbs"
