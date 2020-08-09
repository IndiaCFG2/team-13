from django.db import models

class review(models.Model):
    student_name=models.CharField(max_length=10)
    teacher_name=models.CharField(max_length=10)
    review=models.TextField()
    def __str__(self):
        return self.student_name

# class get_content(models.Model):
#     subject=models.CharField(max_length=10)
#     def __str__(self):
#         return self.subject

class getContent(models.Model):
    subject=models.CharField(max_length=10)
    def __str__(self):
        return self.subject