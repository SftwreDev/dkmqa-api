from django.db import models
from authentication.models import User

from language.models import Language

################# Category 1  ########################

class Category(models.Model):

    steps = models.PositiveIntegerField()
    date_created = models.DateField(auto_now=True, verbose_name="Date Created")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= 'Created by', related_name='category_created')
    date_updated = models.DateField(auto_now=True, verbose_name='Date updated')
    update_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= 'Update by', related_name='category_update')


    class Meta:
        db_table = 'category'



class CategoryTranslation(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name='category_1')
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, verbose_name= 'Language ID', related_name='translation_category_id')
    name = models.CharField(max_length=100, verbose_name= 'Category Translation')

    class Meta:
        db_table = 'category_translation'








