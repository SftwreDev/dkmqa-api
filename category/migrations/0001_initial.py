# Generated by Django 3.1 on 2020-09-09 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Category 1 Label')),
                ('steps', models.PositiveIntegerField()),
                ('date_created', models.DateField(auto_now=True, verbose_name='Date Created')),
                ('date_updated', models.DateField(auto_now=True, verbose_name='Date updated')),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='createdBy', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('update_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='updatedBy', to=settings.AUTH_USER_MODEL, verbose_name='Update by')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('code', models.CharField(max_length=100, verbose_name='Code')),
                ('date_created', models.DateField(auto_now=True, verbose_name='Date Created')),
                ('created_by', models.CharField(max_length=100, verbose_name='Created by')),
                ('date_updated', models.DateField(auto_now=True, verbose_name='Date updated')),
                ('update_by', models.CharField(max_length=100, verbose_name='Update by')),
            ],
        ),
        migrations.CreateModel(
            name='Category3Translation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Category 3 Translation')),
                ('LanguageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.language', verbose_name='Language ID')),
            ],
        ),
        migrations.CreateModel(
            name='Category3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('date_created', models.DateField(auto_now=True, verbose_name='Date Created')),
                ('created_by', models.CharField(max_length=100, verbose_name='Created by')),
                ('date_updated', models.DateField(auto_now=True, verbose_name='Date updated')),
                ('update_by', models.CharField(max_length=100, verbose_name='Update by')),
                ('category1ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category1', verbose_name='Category 1 ID')),
                ('category3Translation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category3translation', verbose_name='Category 2 Transalation')),
            ],
        ),
        migrations.CreateModel(
            name='Category2Translation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Category 2 Translation')),
                ('LanguageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.language', verbose_name='Language ID')),
            ],
        ),
        migrations.CreateModel(
            name='Category2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('date_created', models.DateField(auto_now=True, verbose_name='Date Created')),
                ('created_by', models.CharField(max_length=100, verbose_name='Created by')),
                ('date_updated', models.DateField(auto_now=True, verbose_name='Date updated')),
                ('update_by', models.CharField(max_length=100, verbose_name='Update by')),
                ('category1ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category1', verbose_name='Category 1 ID')),
                ('category2Translation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category2translation', verbose_name='Category 2 Transalation')),
            ],
        ),
        migrations.CreateModel(
            name='Category1Translation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Category 1 Translation')),
                ('LanguageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.language', verbose_name='Language ID')),
            ],
        ),
    ]
