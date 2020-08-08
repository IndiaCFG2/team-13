from django.db import models
from admin_app.models import subject_db
# from django.contrib.auth.models import User

# Create your models here.


# class UserProfileInfo(models.Model):

#     user = models.OneToOneField(User, on_delete=models.CASCADE,)

#     def __str__(self):
#         return self.user.username

# class teacher_content(models.Model):

#     topic = models.CharField(max_length=100, default="",)
#     subject = models.ForeignKey(
#         subject_db, on_delete=models.CASCADE, default="",)
#     files = models.ImageField(upload_to='teacher_app', blank=True)

#     def __str__(self):
#         return self.user.username
