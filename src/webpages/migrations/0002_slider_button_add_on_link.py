# Generated by Django 3.1.7 on 2021-02-20 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='button_add_on_link',
            field=models.URLField(blank=True, max_length=128),
        ),
    ]
