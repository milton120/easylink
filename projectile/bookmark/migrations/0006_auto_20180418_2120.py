# Generated by Django 2.0.4 on 2018-04-18 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0005_auto_20180418_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
