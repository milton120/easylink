# Generated by Django 2.0.4 on 2018-04-18 20:57

import common.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('status', models.IntegerField(choices=[(1, 'ACTIVE'), (2, 'DRAFT'), (3, 'INACTIVE'), (4, 'REMOVED'), (5, 'DENIED')], default=1)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(editable=False, max_length=512, null=True, unique=True)),
                ('description', models.TextField(blank=True)),
                ('priority', models.PositiveIntegerField(default=0, help_text='Highest comes first.')),
                ('entry_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bookmark_category_entry_by', to=settings.AUTH_USER_MODEL, verbose_name='entry by')),
                ('updated_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bookmark_category_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='last updated by')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('status', models.IntegerField(choices=[(1, 'ACTIVE'), (2, 'DRAFT'), (3, 'INACTIVE'), (4, 'REMOVED'), (5, 'DENIED')], default=1)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=512)),
                ('url', models.TextField()),
                ('image', common.fields.TimestampImageField(blank=True, null=True, upload_to='bookmark/link')),
                ('description', models.TextField(blank=True)),
                ('priority', models.PositiveIntegerField(default=0, help_text='Highest comes first.')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='links_of_category', to='bookmark.Category')),
                ('entry_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bookmark_link_entry_by', to=settings.AUTH_USER_MODEL, verbose_name='entry by')),
                ('updated_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bookmark_link_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='last updated by')),
            ],
            options={
                'ordering': ('-updated_at',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('status', models.IntegerField(choices=[(1, 'ACTIVE'), (2, 'DRAFT'), (3, 'INACTIVE'), (4, 'REMOVED'), (5, 'DENIED')], default=1)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(editable=False, max_length=512, null=True, unique=True)),
                ('description', models.TextField(blank=True)),
                ('entry_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bookmark_tag_entry_by', to=settings.AUTH_USER_MODEL, verbose_name='entry by')),
                ('updated_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bookmark_tag_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='last updated by')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='link',
            unique_together={('category', 'url')},
        ),
    ]