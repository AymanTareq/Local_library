from django.db import models

class StudentPaymentInfo(models.Model):
    name_of_month = models.CharField(max_length=15)

    def __str__(self):
        return self.name_of_month

class StudentInfo(models.Model):
    student_name = models.CharField(max_length=20)
    student_class = models.CharField(max_length=5)
    student_institution = models.CharField(max_length=100,blank=True,null=True,help_text='Enter school name.')

    payment_for_month = models.ForeignKey(StudentPaymentInfo, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField(help_text='Payment Amount in Tk.')
    date = models.DateField(help_text="Date of payment.")

    def __str__(self):
        return self.student_name

