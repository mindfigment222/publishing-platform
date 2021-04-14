# Generated by Django 3.1.7 on 2021-04-14 20:00

from django.db import migrations, models
import posts.utils


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20210327_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.FileField(upload_to=posts.utils.get_post_image_dir_path),
        ),
    ]