# Generated by Django 3.1 on 2020-09-29 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('defect_codes', '0003_auto_20200930_0216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='defectcodestranslation',
            old_name='name',
            new_name='descriptions',
        ),
    ]
