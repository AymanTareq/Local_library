# Generated by Django 3.1.1 on 2020-10-08 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stuinfo', '0002_studentinfo_student_institution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='payment_for_month',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stuinfo.studentpaymentinfo'),
        ),
    ]
