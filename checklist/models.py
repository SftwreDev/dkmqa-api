from django.db import models
from authentication.models import User

from category.models import Category, Language

################# Category 2 Translation Choices ########################

class ChecklistTranslation(models.Model):
    
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name= 'Language ID',related_name ='checklist_language')
    name = models.CharField(max_length=100, verbose_name= 'Category 2 Translation')

    class Meta:
        db_table = 'checklist_translation'

################# Category 2 Checklist ########################

class Checklist(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name = 'Category Name', related_name ='checklist_id')
    # category2Translation = models.ForeignKey(Category2Translation, on_delete = models.CASCADE, verbose_name = "Category 2 Transalation")
    steps = models.PositiveIntegerField()
    description = models.CharField(max_length=500,blank=True, null=True, verbose_name="Description")
    date_created = models.DateField(auto_now=True, verbose_name="Date Created")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= 'Created by', related_name='checklist_created')
    date_updated = models.DateField(auto_now=True, verbose_name='Date updated')
    update_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= 'Update by', related_name='checklist_update')
    
    class Meta:
        db_table = 'checklist'
