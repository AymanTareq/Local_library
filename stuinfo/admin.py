from django.contrib import admin
from .models import StudentPaymentInfo, StudentInfo

# admin.site.register(StudentInfo)
@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ('student_name','student_class', 'payment_for_month','amount', 'date')
    list_filter = ('payment_for_month',)


admin.site.register(StudentPaymentInfo)
