# Generated by Django 3.1.1 on 2020-09-23 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20200923_1204'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookLanguageclass',
            new_name='BookLanguage',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='book_langinBook',
            new_name='book_language',
        ),
        migrations.RenameField(
            model_name='booklanguage',
            old_name='book_langinorigin',
            new_name='book_language',
        ),
    ]
