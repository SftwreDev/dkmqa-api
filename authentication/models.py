from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = 'username'


    def get_username(self):
        return self.username

    class Meta:
        db_table = 'user'

class UserRoles(models.Model):
    roles = models.CharField(max_length=100, verbose_name='User Roles')
    date_created = models.DateField(auto_now=True, verbose_name='Created Date')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Created by', related_name = "created_by_id")
    date_updated = models.DateField(auto_now=True, verbose_name='Date Updated')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Updated By ', related_name = "updated_by_id")

    def __str__(self):
        return self.roles
    
    class Meta:
        db_table = 'user_roles'


