# Generated by Django 3.0.8 on 2020-08-08 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_app', '0003_teacher_content_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher_content',
            name='user',
        ),
    ]