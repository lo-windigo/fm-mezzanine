from django.core.urlresolvers import reverse
from django.db import models
from mezzanine.core.models import Orderable
from mezzanine.galleries.models import Gallery, GalleryImage
from mezzanine.pages.models import Page, RichText


class Herb(GalleryImage):
	common  = models.CharField('Herb', max_length=500)
	latin   = models.CharField('Botanical Name', max_length=500)
	price   = models.DecimalField('Dried Per Oz', max_digits=6, decimal_places=2)
	url     = models.SlugField()

	class Meta:
		verbose_name = u"Herb"
		verbose_name_plural = u"Herbs"

	def get_absolute_url(self):
		return reverse("herb", args=[self.url])


class HerbsGallery(Gallery):

	class Meta:
		verbose_name = u"Herb Gallery"
		verbose_name_plural = u"Herb Galleries"

	# This function is part of the magic
	def save(self, *args, **kwargs):
		super(HerbsGallery, self).save(*args, **kwargs)

#	def get_absolute_url(self):
#		return reverse("herb-gallery", args=[self.desc])
