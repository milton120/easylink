import logging
import pytz

from django.db import models

from django.utils.translation import gettext as _
from django.utils.text import slugify

from common.fields import TimestampImageField
from common.models import (
    CreatedAtUpdatedAtBaseModel,
    NameSlugDescriptionBaseModel,
)
id
logger = logging.getLogger(__name__)

class Tag(NameSlugDescriptionBaseModel):
    
    class Meta:
        ordering = ('name',)
        unique_together = (
            'entry_by',
            'name',
        )
    
    def __str__(self):
        return self.get_name()

    def get_name(self):
        return u"#{}: {}".format(self.id, self.name)


class Category(NameSlugDescriptionBaseModel):
    priority = models.PositiveIntegerField(default=0, help_text='Highest comes first.')
    class Meta:
        ordering = ('-updated_at',)
        verbose_name_plural = "Categories"
        unique_together = (
            'entry_by',
            'name',
        )
    
    def __str__(self):
        return self.get_name()

    def get_name(self):
        return u"#{}: {}".format(self.id, self.name)
    

class Link(CreatedAtUpdatedAtBaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    url = models.TextField(blank=False, null=False)
    slug = models.SlugField(max_length=1024, unique=True, null=True, editable=False)
    image = TimestampImageField(
        upload_to='bookmark/link', blank=True, null=True)
    description = models.TextField(blank=True)
    # note: create_or_select a Anonymous category if user willing not to create a category
    category = models.ForeignKey(
       Category, models.DO_NOTHING, blank=True, null=True,
       related_name='links_of_category' 
    )
    priority = models.PositiveIntegerField(default=0, help_text='Highest comes first.')

    class Meta:
        ordering = ('-updated_at',)
        unique_together = (
            'entry_by',
            'category',
            'url',
        )
    
    def __str__(self):
        return self.get_name()

    def get_name(self):
        return u"#{}: {}".format(self.name, self.id)
    
    def save(self, *args, **kwargs):
        if self.name:
            self.slug = slugify(self.name, allow_unicode=True)
        if not self.name:
                self.name = self.url[:255]
                self.slug = slugify(self.name, allow_unicode=True)

        if not self.category:
            self.category, _ = Category.objects.get_or_create(name="unnamed")
        super(Link, self).save(*args, **kwargs)

