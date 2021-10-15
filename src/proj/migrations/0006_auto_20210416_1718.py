# Generated by Django 3.1.7 on 2021-04-16 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0005_auto_20210313_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='location',
            field=models.CharField(default='Dubai , UAE ', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]