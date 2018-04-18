# Generated by Django 2.0.4 on 2018-04-18 21:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookmark', '0002_auto_20180418_2109'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('entry_by', 'name')},
        ),
    ]
