# Generated by Django 4.0.4 on 2022-06-04 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='durarion',
            new_name='duration',
        ),
    ]
