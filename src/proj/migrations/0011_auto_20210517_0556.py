# Generated by Django 3.1.7 on 2021-05-17 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0010_project_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='budjet',
            new_name='budget',
        ),
    ]