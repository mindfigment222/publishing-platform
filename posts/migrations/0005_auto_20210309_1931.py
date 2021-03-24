# Generated by Django 3.1.7 on 2021-03-09 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('posts', '0004_auto_20210309_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='content_type',
            field=models.ForeignKey(default=19, limit_choices_to=models.Q(models.Q(('app_label', 'posts'), ('model', 'text')), models.Q(('app_label', 'posts'), ('model', 'video')), models.Q(('app_label', 'posts'), ('model', 'image')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
            preserve_default=False,
        ),
    ]
