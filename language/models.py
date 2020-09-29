from django.db import models
from authentication.models import User


# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length = 200 , verbose_name = 'Name')
    code = models.CharField(max_length = 200 , verbose_name = 'Code')
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'language_created_by')
    date_updated = models.DateField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='language_updated_by')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'language'