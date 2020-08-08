from django import forms
from django.contrib.auth.models import User
from admin_app.models import Teacher_db, Student_db


class UserForm_teacher(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm_teacher(forms.ModelForm):
    class Meta():
        model = Teacher_db
        fields = ('name', 'lastname', 'state',
                  'district', 'school', 'language', 'subject')


class UserForm_student(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm_student(forms.ModelForm):
    class Meta():
        model = Student_db
        fields = ('name', 'lastname', 'state', 'district',
                  'school', 'language', 'subject', 'teacher')
