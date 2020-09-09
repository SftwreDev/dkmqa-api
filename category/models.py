from django.db import models
from authentication.models import User

class Language(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    code = models.CharField(max_length=100, verbose_name="Code")
    date_created = models.DateField(auto_now = True, verbose_name="Date Created") 
    created_by = models.CharField(max_length=100, verbose_name='Created by')  # Sample Fields
    date_updated = models.DateField(auto_now=True, verbose_name='Date updated') 
    update_by = models.CharField(max_length=100, verbose_name="Update by") # Sample Fields


################# Category 1 Translation Choices ########################

class Category1Translation(models.Model):
    
    LanguageID = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name= 'Language ID')
    name = models.CharField(max_length=100, verbose_name= 'Category 1 Translation')



################# Category 1 Choices ########################

class Category1(models.Model):
    # category1Translation = models.ForeignKey(Category1Translation, on_delete=models.CASCADE, verbose_name="Category 1 ID")
    name = models.CharField(max_length = 200, verbose_name = "Category 1 Label")
    steps = models.PositiveIntegerField()
    date_created = models.DateField(auto_now=True, verbose_name="Date Created")
    created_by = models.CharField(max_length=100, verbose_name= 'Created by')
    date_updated = models.DateField(auto_now=True, verbose_name='Date updated')
    update_by = models.CharField(max_length=100, verbose_name='Update by')

    
    def __str__(self):
        return self.name
    

################# Category 2 Translation Choices ########################

class Category2Translation(models.Model):
    
    LanguageID = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name= 'Language ID')
    name = models.CharField(max_length=100, verbose_name= 'Category 2 Translation')


################# Category 2 Checklist ########################

class Category2(models.Model):
    category1ID = models.ForeignKey(Category1, on_delete=models.CASCADE, verbose_name = 'Category 1 ID')
    # category2Translation = models.ForeignKey(Category2Translation, on_delete = models.CASCADE, verbose_name = "Category 2 Transalation")
    steps = models.PositiveIntegerField()
    description = models.CharField(max_length=500, verbose_name="Description")
    date_created = models.DateField(auto_now=True, verbose_name="Date Created")
    created_by = models.CharField(max_length=100, verbose_name= 'Created by')
    



################# Category 2 Translation Choices ########################

class Category3Translation(models.Model):
    
    LanguageID = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name= 'Language ID')
    name = models.CharField(max_length=100, verbose_name= 'Category 3 Translation')


################# Category 2 Checklist ########################

class Category3(models.Model):
    category1ID = models.ForeignKey(Category1, on_delete=models.CASCADE, verbose_name = 'Category 1 ID')
    # category3Translation = models.ForeignKey(Category3Translation, on_delete = models.CASCADE, verbose_name = "Category 2 Transalation")
    steps = models.PositiveIntegerField()
    description = models.CharField(max_length=500, verbose_name="Description")
    date_created = models.DateField(auto_now=True, verbose_name="Date Created")
    created_by = models.CharField(max_length=100, verbose_name= 'Created by')
    # date_updated = models.DateField(auto_now=True, verbose_name='Date updated')
    # update_by = models.CharField(max_length=100, verbose_name='Update by')






