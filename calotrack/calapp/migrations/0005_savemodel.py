# Generated by Django 5.0 on 2024-01-31 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calapp', '0004_delete_mainmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='savemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.FloatField()),
                ('protien', models.FloatField()),
                ('carbs', models.FloatField()),
                ('fat', models.FloatField()),
                ('nutrients', models.FloatField()),
                ('vitamins', models.CharField(max_length=50)),
            ],
        ),
    ]
