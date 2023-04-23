# Generated by Django 4.2 on 2023-04-21 22:42

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterField(
            model_name='city',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]