from django.contrib import admin

from CareerGuidanceApp.models import Add_course, Feedback, HRTable, Job_applied_users, LoginTable, Take_quiz, Upload_resume, UserTable, add_certificate, enroll_course, jobTable, view_and_enroll_course

# Register your models here.
admin.site.register(LoginTable),
admin.site.register(UserTable),
admin.site.register(HRTable),
admin.site.register(jobTable),
admin.site.register(add_certificate),
admin.site.register(Add_course),
admin.site.register(Feedback),
admin.site.register(Job_applied_users),
admin.site.register(Upload_resume),
admin.site.register(Take_quiz),
admin.site.register(view_and_enroll_course),



