from django.db import models
from authentication.models import User

from category.models import Category, CategoryTranslation
from language.models import Language

# from rest_framework_tricks.models.fields import NestedProxyField

################# Category 2 Checklist ########################

class Checklist(models.Model):
    category = models.ForeignKey(CategoryTranslation, on_delete=models.CASCADE, verbose_name = 'Category Name', related_name ='checklist_category')
    steps = models.PositiveIntegerField()
    date_created = models.DateField(auto_now=True, verbose_name="Date Created")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= 'Created by', related_name='checklist_created')
    date_updated = models.DateField(auto_now=True, verbose_name='Date updated')
    update_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= 'Update by', related_name='checklist_update')
    
    class Meta:
        db_table = 'checklist'


################# Category 2 Translation Choices ########################

class ChecklistTranslation(models.Model):
    
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name= 'Language ID',related_name ='checklist_translation_language')
    description = models.CharField(max_length=100, verbose_name= 'Category 2 Translation')
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE, related_name = 'checklist_translation')

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'checklist_translation'

