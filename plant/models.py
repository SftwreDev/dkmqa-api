from django.db import models
from authentication.models import User
from client.models import Client
from person.models import Person


class Address(models.Model):
    street_1 = models.CharField(max_length=100, verbose_name = 'Street 1')
    street_2 = models.CharField(max_length=100, verbose_name = 'Street 2')
    city = models.CharField(max_length=100, verbose_name= 'City')
    state = models.CharField(max_length=100, verbose_name='State')
    zipcode = models.CharField(max_length=100, verbose_name='ZipCode')
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'address_created_by')
    date_updated = models.DateField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address_updated_by')

    def __str__(self):
        return self.street_1 + '' + self.street_2 + '' + self.city


class Plant(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name= 'Client', related_name='plant_client')
    name = models.CharField(max_length=100, verbose_name='Name')
    contact_person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name = 'Contact Person', related_name='plant_contact_person')
    address = models.ForeignKey(Address, on_delete = models.CASCADE, verbose_name = 'Address', related_name='plant_address' )
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'plant_created_by')
    date_updated = models.DateField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plant_updated_by')


    def __str__(self):
        return self.name