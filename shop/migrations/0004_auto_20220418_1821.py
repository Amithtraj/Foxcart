# Generated by Django 2.2 on 2022-04-18 12:51

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('shop', '0003_auto_20220418_1732'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='catogories',
            new_name='categories',
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]