# Generated by Django 3.1 on 2020-09-22 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShiftCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_code', models.CharField(max_length=100, verbose_name='Shift Code')),
                ('date_created', models.DateField(auto_now=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_shift_code', to='client.client')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shift_code_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shift_code_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_hour_no', models.PositiveIntegerField(verbose_name='Shift Hour No')),
                ('shift_hour', models.TimeField(verbose_name='Shift Hour')),
                ('description', models.CharField(max_length=500, verbose_name='Description')),
                ('start_time', models.TimeField(verbose_name='Start Time')),
                ('end_time', models.TimeField(verbose_name='End Time')),
                ('date_created', models.DateField(auto_now=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_shift', to='client.client')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shift_created_by', to=settings.AUTH_USER_MODEL)),
                ('shift_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='code_id', to='shift.shiftcode')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shift_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
