# Generated by Django 3.2.10 on 2022-01-18 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20220118_1145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fatherstudentmodels',
            old_name='full_name',
            new_name='father_full_name',
        ),
        migrations.RenameField(
            model_name='motherstudentmodels',
            old_name='full_name',
            new_name='mother_full_name',
        ),
    ]
