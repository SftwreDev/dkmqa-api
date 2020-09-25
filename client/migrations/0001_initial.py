# Generated by Django 3.1 on 2020-09-25 12:46

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
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Date Created')),
                ('updated_date', models.DateField(auto_now_add=True, verbose_name='Date Updated')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_client', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='update_client', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'db_table': 'client',
            },
        ),
    ]
