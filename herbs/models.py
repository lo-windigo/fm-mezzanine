from __future__ import unicode_literals
from future.builtins import str
from future.utils import native

from io import BytesIO
import os
from string import punctuation
from zipfile import ZipFile

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
try:
	from django.utils.encoding import force_text
except ImportError:
	# Django < 1.5
	from django.utils.encoding import force_unicode as force_text
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import settings
from mezzanine.core.fields import FileField
from mezzanine.core.models import Orderable, RichText
from mezzanine.pages.models import Page
from mezzanine.utils.importing import import_dotted_path
from mezzanine.utils.models import upload_to


# Set the directory where gallery images are uploaded to,
# either MEDIA_ROOT + 'galleries', or filebrowser's upload
# directory if being used.
GALLERIES_UPLOAD_DIR = "galleries"
if settings.PACKAGE_NAME_FILEBROWSER in settings.INSTALLED_APPS:
	fb_settings = "%s.settings" % settings.PACKAGE_NAME_FILEBROWSER
	try:
		GALLERIES_UPLOAD_DIR = import_dotted_path(fb_settings).DIRECTORY
	except ImportError:
		pass


class HerbGallery(Page, RichText):
	"""
	Page of herbs
	"""

	class Meta:
		verbose_name = _("Herb Gallery")
		verbose_name_plural = _("Herb Galleries")


class Herb(models.Model):
	"""
	A single herb
	"""

	gallery = models.ManyToManyField(HerbGallery, blank=True)
	file = FileField(_("File"), max_length=200, format="Image",
		upload_to=upload_to("herbs.Herb.file", "herbs"), blank=True)
	herb = models.CharField(_("Herb"), max_length=1000, blank=True)
	latin = models.CharField(_("Latin"), max_length=1000, blank=True)
	price_per_oz = models.DecimalField(_("Price Per Oz"), max_digits=9,
		decimal_places=2, blank=True)

	class Meta:
		ordering = ('herb', 'latin',)
		verbose_name = _("Herb")
		verbose_name_plural = _("Herbs")


	def __unicode__(self, *args, **kwargs):
		return self.herb


	def save(self, *args, **kwargs):
		"""
		If no herb name is given when created, create one from the
		file name.
		"""
		if not self.id and not self.herb:
			name = force_text(self.file.name)
			name = name.rsplit("/", 1)[-1].rsplit(".", 1)[0]
			name = name.replace("'", "")
			name = "".join([c if c not in punctuation else " " for c in name])
			# str.title() doesn't deal with unicode very well.
			# http://bugs.python.org/issue6412
			name = "".join([s.upper() if i == 0 or name[i - 1] == " " else s
							for i, s in enumerate(name)])
			self.herb = name
		super(Herb, self).save(*args, **kwargs)
