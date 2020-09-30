# Generated by Django 3.1 on 2020-09-30 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0002_auto_20200925_0021'),
        ('category', '0002_auto_20200930_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytranslation',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='translation_category_id', to='language.language', verbose_name='Language ID'),
            preserve_default=False,
        ),
    ]
