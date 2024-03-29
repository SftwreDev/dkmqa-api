from django.db import models
from authentication.models import User
from category.models import Category, Language
from language.models import Language



################# Defect Codes ########################

class Defectcodes(models.Model):

    steps = models.PositiveIntegerField()
    date_created = models.DateField(auto_now=True, verbose_name="Date Created")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= 'Created by', related_name='defect_codes_created')
    date_updated = models.DateField(auto_now=True, verbose_name='Date updated')
    update_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= 'Update by', related_name='defect_codes_update')

    class Meta:
        db_table = 'defect_codes'

################# Defect Codes Translations ########################

class DefectcodesTranslation(models.Model):
    defect_code = models.ForeignKey(Defectcodes, on_delete=models.CASCADE,related_name = 'defect_code_translation')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name= 'Language ID',related_name ='defect_codes_language')
    description = models.CharField(max_length=100, verbose_name= 'Category 3 Translation')

    class Meta:
        db_table = 'defect_codes_translations'
