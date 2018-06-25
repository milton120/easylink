# Generated by Django 2.0.4 on 2018-06-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0009_link_is_global'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_global',
            field=models.IntegerField(choices=[(1, 'GLOBAL'), (2, 'PRIVATE'), (3, 'WAS PRIVATE NOW GLOBAL'), (4, 'WAS GLOBAL NOW PRIVATE'), (5, 'SHARED WITH FRIENDS')], default=2),
        ),
    ]
