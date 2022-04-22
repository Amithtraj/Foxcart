# Generated by Django 2.2 on 2022-04-18 10:26

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='catogories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
    ]