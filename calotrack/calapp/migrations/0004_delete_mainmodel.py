# Generated by Django 5.0 on 2024-01-31 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calapp', '0003_rename_name_mainmodel_inpname_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='mainmodel',
        ),
    ]
