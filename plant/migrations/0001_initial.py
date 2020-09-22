# Generated by Django 3.1 on 2020-09-18 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('person', '0002_auto_20200919_0011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_1', models.CharField(max_length=100, verbose_name='Street 1')),
                ('street_2', models.CharField(max_length=100, verbose_name='Street 2')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('state', models.CharField(max_length=100, verbose_name='State')),
                ('zipcode', models.CharField(max_length=100, verbose_name='ZipCode')),
                ('date_created', models.DateField(auto_now=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('date_created', models.DateField(auto_now=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plant_address', to='plant.address', verbose_name='Address')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plant_client', to='client.client', verbose_name='Client')),
                ('contact_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plant_contact_person', to='person.person', verbose_name='Contact Person')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plant_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plant_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]