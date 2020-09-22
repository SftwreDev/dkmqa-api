from django.db import models
from authentication.models import User
from category.models import Category, Language

class DefectcodesTranslation(models.Model):
    
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name= 'Language ID',related_name ='defect_codes_language')
    name = models.CharField(max_length=100, verbose_name= 'Category 3 Translation')

    class Meta:
        managed = False
        db_table = 'defect_codes_translation'

################# Category 2 Checklist ########################

class Defectcodes(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name = 'Category Name', related_name ='defect_codes_id')
    # category3Translation = models.ForeignKey(Category3Translation, on_delete = models.CASCADE, verbose_name = "Category 2 Transalation")
    steps = models.PositiveIntegerField()
    description = models.CharField(max_length=500, verbose_name="Description")
    date_created = models.DateField(auto_now=True, verbose_name="Date Created")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= 'Created by', related_name='defect_codes_created')
    date_updated = models.DateField(auto_now=True, verbose_name='Date updated')
    update_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= 'Update by', related_name='defect_codes_update')

    class Meta:
        db_table = 'defect_codes'