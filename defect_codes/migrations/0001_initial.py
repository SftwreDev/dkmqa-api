# Generated by Django 3.1 on 2020-09-17 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefectcodesTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Category 3 Translation')),
            ],
            options={
                'db_table': 'defect_codes_translation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Defectcodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steps', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=500, verbose_name='Description')),
                ('date_created', models.DateField(auto_now=True, verbose_name='Date Created')),
                ('date_updated', models.DateField(auto_now=True, verbose_name='Date updated')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='defect_codes_id', to='category.category', verbose_name='Category Name')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='defect_codes_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('update_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='defect_codes_update', to=settings.AUTH_USER_MODEL, verbose_name='Update by')),
            ],
            options={
                'db_table': 'defect_codes',
            },
        ),
    ]