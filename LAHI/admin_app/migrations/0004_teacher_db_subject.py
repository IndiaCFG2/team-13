# Generated by Django 3.0.8 on 2020-08-08 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0003_remove_teacher_db_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_db',
            name='subject',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='admin_app.subject_db'),
        ),
    ]
