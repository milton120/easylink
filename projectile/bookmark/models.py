import logging
import pytz

from django.db import models

from django.utils.translation import gettext as _
from django.utils.text import slugify
from django.db.models import Q
from django.core.exceptions import ValidationError

from common.validators import url_validator
from common.utils import slug_generator, get_website_title
from common.enums import PublishStatus, Status
from common.fields import TimestampImageField
from common.models import (
    CreatedAtUpdatedAtBaseModel,
    NameSlugDescriptionBaseModel,
)
from core.models import Person

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
    is_global = models.IntegerField(
        choices=[(choice.value, choice.name.replace("_", " ")) for choice in PublishStatus],
        default=PublishStatus.PRIVATE.value)
    class Meta:
        ordering = ('-updated_at',)
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.get_name()

    def get_name(self):
        return u"#{}: {}".format(self.id, self.name)
    
    def clean(self):
        if self.name and self.entry_by:
            if not self.pk:
                query = Category.objects.filter(
                    status=Status.ACTIVE.value,
                    name=self.name,
                    entry_by=self.entry_by.pk
                ).exists()
            if self.pk:
                query = Category.objects.filter(
                    ~Q(pk=self.pk) &
                    Q(name__iexact=self.name) &
                    Q(status=Status.ACTIVE.value) &
                    Q(entry_by=self.entry_by.pk)
                ).exists()
            if query:
                raise ValidationError(
                    {'name': _(
                        "Category Name #{} already exists.".format(
                            self.name
                        )
                    )}
                )
    

class Link(CreatedAtUpdatedAtBaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    url = models.TextField(blank=False, null=False, validators=[url_validator])
    slug = models.SlugField(max_length=1024, unique=True, null=True, editable=False)
    image = TimestampImageField(
        upload_to='bookmark/link', blank=True, null=True)
    description = models.TextField(blank=True)
    # note: create_or_select a Anonymous category if user willing not to create a category
    category = models.ForeignKey(
        Category, models.DO_NOTHING, blank=True, null=True,
        related_name='links_of_category' 
    )
    tags = models.ManyToManyField(
        Tag, through='bookmark.LinkTag', related_name='link_of_tag')
    priority = models.PositiveIntegerField(default=0, help_text='Highest comes first.')
    is_global = models.IntegerField(
        choices=[(choice.value, choice.name.replace("_", " ")) for choice in PublishStatus],
        default=PublishStatus.PRIVATE.value)

    class Meta:
        ordering = ('-updated_at',)
    
    def __str__(self):
        return self.get_name()

    def get_name(self):
        return u"#{}: {}".format(self.name, self.id)
    
    def save(self, *args, **kwargs):
        if self.name:
            self.slug = self.slug = slug_generator(self.name[:128], self.__class__)
        if not self.name:
            self.name = get_website_title(self.url)
            self.slug = slug_generator(self.name, self.__class__)

        if not self.category:
            self.category, _ = Category.objects.get_or_create(
                name="unnamed", entry_by=Person.get_anonymous_user(),
                is_global=PublishStatus.GLOBAL.value)
        super(Link, self).save(*args, **kwargs)


class LinkTag(CreatedAtUpdatedAtBaseModel):
    link = models.ForeignKey(
        Link, models.DO_NOTHING, blank=True, null=True,
        related_name='tag_link' 
    )
    tag = models.ForeignKey(
        Tag, models.DO_NOTHING, blank=True, null=True,
        related_name='link_tag' 
    )

    # pylint: disable=old-style-class, no-init
    class Meta:
        verbose_name = "Tag to Link"
        verbose_name_plural = "Tags to Link"

    def __str__(self):
        return self.get_name()

    def get_name(self):
        return u"#{}: {} / {}".format(self.id, self.link, self.tag)
