# Generated by Django 5.1.3 on 2024-11-28 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_rename_image_about_image1_about_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image3',
            field=models.ImageField(default=1, upload_to='about/'),
            preserve_default=False,
        ),
    ]
