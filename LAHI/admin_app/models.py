from django.db import models

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
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    school = models.ForeignKey(school_db, on_delete=models.CASCADE,)
    language = models.CharField(max_length=100)
    subject = models.ForeignKey(
        subject_db, on_delete=models.CASCADE, default="",)

    def __str__(self):
        return self.username


class Student_db(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    school = models.ForeignKey(school_db, on_delete=models.CASCADE,)
    language = models.CharField(max_length=100)
    subject = models.ForeignKey(subject_db, on_delete=models.CASCADE,)
    teacher = models.ForeignKey(Teacher_db, on_delete=models.CASCADE,)

    def __str__(self):
        return self.username
