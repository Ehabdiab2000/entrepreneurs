# Generated by Django 3.1.7 on 2021-04-16 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0007_join'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply_project', to='proj.project'),
        ),
    ]
