# Generated by Django 2.0.4 on 2018-04-18 21:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookmark', '0007_auto_20180418_2120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('-updated_at',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together={('entry_by', 'name')},
        ),
    ]