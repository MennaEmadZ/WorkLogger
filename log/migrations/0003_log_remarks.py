# Generated by Django 4.0.4 on 2022-06-05 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_rename_durarion_log_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='remarks',
            field=models.CharField(max_length=200, null=True),
        ),
    ]