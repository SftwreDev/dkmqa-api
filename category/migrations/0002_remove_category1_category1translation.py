# Generated by Django 3.1 on 2020-09-01 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category1',
            name='category1Translation',
        ),
    ]