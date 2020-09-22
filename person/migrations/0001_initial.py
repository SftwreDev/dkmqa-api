# Generated by Django 3.1 on 2020-09-18 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
# import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('middle_name', models.CharField(max_length=100, verbose_name='Middle Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('position', models.CharField(max_length=100, verbose_name='Position')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('contact_no', models.CharField(max_length=100, verbose_name='Contact No')),
                ('date_created', models.DateField(auto_now=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
        ),
    ]
