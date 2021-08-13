# Generated by Django 3.1.7 on 2021-02-20 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_slider_button_add_on_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('fb_link', models.URLField(blank=True, max_length=128)),
                ('insta_link', models.URLField(blank=True, max_length=128)),
                ('photo', models.ImageField(upload_to='media/team/%Y/%m/%d/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='slider',
            name='photo',
            field=models.ImageField(upload_to='media/slider/%Y/%m/'),
        ),
    ]
