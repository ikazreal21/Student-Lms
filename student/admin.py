from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(StudentProfile)
admin.site.register(Subject)
admin.site.register(StudGrades)
admin.site.register(Reminder)

# Prof admin

# admin.site.register(ProfessProfile)
# admin.site.register(Schoolworks)
# admin.site.register(Grades)
# admin.site.register(Profsub)
# admin.site.register(Schedule)
