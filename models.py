from django.db import models

class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)
from django.db import models

# Create your models here.
class school_info(models.Model):
    sname=models.CharField(max_length=20)
    def __str__(self):
        return self.sname
class subjects(models.Model):
    subname=models.CharField(max_length=10)
    def __str__(self):
        return self.subname


class teacher_info(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    school=models.ForeignKey(school_info, on_delete=models.CASCADE, null=True)
    interested_subject1=models.ForeignKey(subjects,max_length=10)
    #interested_subject2=models.ForeignKey(subjects,max_length=10)
    #interested_subject3=models.ForeignKey(subjects, max_length=10)
    def __str__(self):
        return self.name

class content_info(models.Model):
    lsubject=models.ForeignKey(subjects,max_length=20)
    llink=models.CharField()
    def __str__(self):
        return self.lsubject