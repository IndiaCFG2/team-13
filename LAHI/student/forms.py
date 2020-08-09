from django import forms
from .models import review,getContent

class review_form(forms.ModelForm):
    class Meta():
        model = review
        fields = ('student_name','teacher_name','review')

# class get_contentForm(forms.ModelForm):
#     class Meta():
#         model = get_content
#         fields = ('subject',)

class get_contentForm(forms.ModelForm):
    class Meta():
        model = getContent
        fields = ('subject',)
