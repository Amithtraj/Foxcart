# Generated by Django 2.2 on 2022-04-18 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('shop', '0002_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='available',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='catogoriesf',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.catogories'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]