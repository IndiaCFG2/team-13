# Generated by Django 3.0.8 on 2020-08-08 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teacher_app', '0002_auto_20200808_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_content',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
