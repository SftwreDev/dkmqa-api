from django.db import models
from authentication.models import User
from client.models import Client


class ShiftCode(models.Model):
    client = models.ForeignKey(Client, on_delete = models.CASCADE, related_name='client_shift_code')
    shift_code = models.CharField(max_length=100, verbose_name='Shift Code')
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'shift_code_created_by')
    date_updated = models.DateField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'shift_code_updated_by')

    def __str__(self):
        return self.shift_code

    class Meta:
        db_table = 'shift_code'
    

class Shift(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_shift')
    shift_code = models.ForeignKey(ShiftCode, on_delete = models.CASCADE, related_name='code_id')
    shift_hour_no = models.PositiveIntegerField(verbose_name = 'Shift Hour No')
    shift_hour = models.TimeField(auto_now=False,verbose_name = 'Shift Hour')
    description = models.CharField(max_length=500,verbose_name = 'Description') 
    start_time = models.TimeField(auto_now=False,verbose_name = 'Start Time')
    end_time = models.TimeField(auto_now=False,verbose_name = 'End Time')
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'shift_created_by')
    date_updated = models.DateField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'shift_updated_by')

    def __str__(self):
        return self.description
    
    class Meta:
        db_table = 'shift'