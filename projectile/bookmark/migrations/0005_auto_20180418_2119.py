# Generated by Django 2.0.4 on 2018-04-18 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0004_auto_20180418_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]