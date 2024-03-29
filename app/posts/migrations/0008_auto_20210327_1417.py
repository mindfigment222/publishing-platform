# Generated by Django 3.1.7 on 2021-03-27 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('posts', '0007_auto_20210310_1331'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Video',
        ),
        migrations.AlterField(
            model_name='section',
            name='content_type',
            field=models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'posts'), ('model', 'title')), models.Q(('app_label', 'posts'), ('model', 'subtitle')), models.Q(('app_label', 'posts'), ('model', 'text')), models.Q(('app_label', 'posts'), ('model', 'citation')), models.Q(('app_label', 'posts'), ('model', 'image')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]
