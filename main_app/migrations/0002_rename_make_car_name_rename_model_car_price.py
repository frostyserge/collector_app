# Generated by Django 4.2.2 on 2023-06-26 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='make',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='model',
            new_name='price',
        ),
    ]