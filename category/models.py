from django.db import models
from authentication.models import User

class Language(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    code = models.CharField(max_length=100, verbose_name="Code")
    date_created = models.DateField(auto_now = True, verbose_name="Date Created") 
    created_by = models.CharField(max_length=100, verbose_name='Created by')  # Sample Fields
    date_updated = models.DateField(auto_now=True, verbose_name='Date updated') 
    update_by = models.CharField(max_length=100, verbose_name="Update by") # Sample Fields

    class Meta:
        managed = False
        db_table = 'language'

################# Category 1 Translation Choices ########################

class CategoryTranslation(models.Model):
    
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name= 'Language ID')
    name = models.CharField(max_length=100, verbose_name= 'Category 1 Translation')

    class Meta:
        db_table = 'category_translation'


class Category(models.Model):
    # category1Translation = models.ForeignKey(Category1Translation, on_delete=models.CASCADE, verbose_name="Category 1 ID")
    name = models.CharField(max_length = 200, verbose_name = "Category 1 Label")
    steps = models.PositiveIntegerField()
    date_created = models.DateField(auto_now=True, verbose_name="Date Created")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= 'Created by', related_name='category_created')
    date_updated = models.DateField(auto_now=True, verbose_name='Date updated')
    update_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= 'Update by', related_name='category_update')

    
    def __str__(self):
        return self.name
    
    

    class Meta:
        db_table = 'category'





