# Generated by Django 3.1.7 on 2021-04-16 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0008_auto_20210416_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='join',
            name='cover_letter',
        ),
        migrations.AddField(
            model_name='join',
            name='message',
            field=models.TextField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
