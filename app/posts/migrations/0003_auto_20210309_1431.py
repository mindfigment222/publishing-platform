# Generated by Django 3.1.7 on 2021-03-09 14:31

from django.db import migrations

import posts.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_image_section_text_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='section',
            name='order',
            field=posts.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
