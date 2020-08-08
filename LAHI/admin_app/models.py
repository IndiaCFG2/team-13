from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class school_db(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class subject_db(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Teacher_db(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, default="",)

    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    school = models.ForeignKey(school_db, on_delete=models.CASCADE,)
    language = models.CharField(max_length=100)
    subject = models.ForeignKey(
        subject_db, on_delete=models.CASCADE, default="",)

    def __str__(self):
        return self.user.username


class Student_db(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, default="",)

    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    school = models.ForeignKey(school_db, on_delete=models.CASCADE,)
    language = models.CharField(max_length=100)
    subject = models.ForeignKey(subject_db, on_delete=models.CASCADE,)
    teacher = models.ForeignKey(Teacher_db, on_delete=models.CASCADE,)

    def __str__(self):
        return self.user.username


class content_db(models.Model):
    subject = models.ForeignKey(subject_db, on_delete=models.CASCADE,)
    files = models.ImageField(upload_to='admin_app')


# class content_db_files(models.Model):
#     files = models.FileField(upload_to="admin_app")
#     feed = models.ForeignKey(
#         content_db, on_delete=models.CASCADE, related_name='files')
