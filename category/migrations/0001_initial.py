# Generated by Django 3.1 on 2020-09-14 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Category 1 Label')),
                ('steps', models.PositiveIntegerField()),
                ('date_created', models.DateField(auto_now=True, verbose_name='Date Created')),
                ('created_by', models.CharField(max_length=100, verbose_name='Created by')),
                ('date_updated', models.DateField(auto_now=True, verbose_name='Date updated')),
                ('update_by', models.CharField(max_length=100, verbose_name='Update by')),
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
                ('steps', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=500, verbose_name='Description')),
                ('date_created', models.DateField(auto_now=True, verbose_name='Date Created')),
                ('created_by', models.CharField(max_length=100, verbose_name='Created by')),
                ('categoryName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='defect_codes', to='category.category1', verbose_name='Category Name')),
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
                ('steps', models.PositiveIntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Description')),
                ('date_created', models.DateField(auto_now=True, verbose_name='Date Created')),
                ('created_by', models.CharField(blank=True, max_length=100, null=True, verbose_name='Created by')),
                ('categoryID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='checklist', to='category.category1', verbose_name='Category Name')),
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
