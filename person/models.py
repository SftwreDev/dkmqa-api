from django.db import models

from authentication.models import User


class Person(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    middle_name = models.CharField(max_length=100, verbose_name='Middle Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    position = models.CharField(max_length=100, verbose_name = 'Position')
    email = models.EmailField(verbose_name='Email')
    contact_no = models.CharField(max_length=20, verbose_name='Phone number')
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Created by', related_name='person_created_by')
    date_updated = models.DateField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Updated by',  related_name='person_updated_by')


    def __str__(self):
        return self.last_name + ',' + self.first_name + ' ' + self.middle_name
    
    class Meta:
        db_table = 'person'


