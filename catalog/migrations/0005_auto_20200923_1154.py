# Generated by Django 3.1.1 on 2020-09-23 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20200923_1151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_lang',
            new_name='book_langinBook',
        ),
        migrations.RenameField(
            model_name='booklanguageclass',
            old_name='book_lang',
            new_name='book_langinorigin',
        ),
    ]
