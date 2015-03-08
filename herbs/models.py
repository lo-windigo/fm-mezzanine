from django.core.urlresolvers import reverse
from django.db import models
import Image
from mezzanine.core.models import Orderable
from mezzanine.pages.models import Page, RichText

THUMBNAIL_SIZE = 175, 175

class HerbGallery(Page):

	#herbs = models.ManyToManyField(Herb)

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
	image   = models.ImageField("Picture", blank=True, upload_to="herbs/images/")
	thumb   = models.ImageField("Thumbnail", blank=True, editable=False,
			upload_to="herbs/thumbs/")
	common  = models.CharField("Herb", max_length=500)
	c_slug  = models.SlugField(max_length=100)
	latin   = models.CharField('Botanical Name', max_length=500)
	l_slug  = models.SlugField(max_length=100)
	price   = models.DecimalField('Dried Per Oz', max_digits=6, decimal_places=2)
	gallery = models.ForeignKey(HerbGallery, blank=True)
	#galleries = models.ManyToManyField(HerbGallery)

	class Meta:
		verbose_name = u"Herb"
		verbose_name_plural = u"Herbs"

	def save(self, *args, **kwargs):

		try:
			# Open the image
			herbImage = self.image.filename.open(mode='rb')

			# Resize the image to thumbnail size
			thumb = herbImage.thumbnail(THUMBNAIL_SIZE)

			# Save the thumbnail to the database/file system
			self.thumb.save(self.image.name, thumb)

		except IOError:
			pass

		# Save the field normally
		super(Herb, self).save(*args, **kwargs)
