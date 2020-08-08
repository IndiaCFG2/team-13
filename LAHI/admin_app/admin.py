from django.contrib import admin
from .models import school_db, subject_db, Teacher_db, Student_db, content_db
# Register your models here.

admin.site.register(subject_db)
admin.site.register(Teacher_db)
admin.site.register(school_db)
admin.site.register(Student_db)
admin.site.register(content_db)
