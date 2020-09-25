from django.db import models
from authentication.models import User


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    created_date = models.DateField(auto_now_add=True, verbose_name='Date Created')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Created by', related_name = 'create_client')
    updated_date = models.DateField(auto_now_add=True, verbose_name='Date Updated')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Updated by', related_name = 'update_client')
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'client'