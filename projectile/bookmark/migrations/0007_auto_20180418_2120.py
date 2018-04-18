# Generated by Django 2.0.4 on 2018-04-18 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0006_auto_20180418_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='links_of_category', to='bookmark.Category'),
        ),
    ]