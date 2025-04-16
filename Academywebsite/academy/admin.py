from django.contrib import admin
from .models import Student, Course, Instructor, Category, Enrollment, Assignment, Submission

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Category)
admin.site.register(Enrollment)
admin.site.register(Assignment)
admin.site.register(Submission)
