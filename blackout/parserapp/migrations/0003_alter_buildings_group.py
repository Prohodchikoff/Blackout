# Generated by Django 4.1.4 on 2023-03-27 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parserapp', '0002_alter_buildings_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildings',
            name='Group',
            field=models.CharField(blank=True, choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third')], max_length=10, verbose_name='Group'),
        ),
    ]
