# Generated by Django 3.2.10 on 2022-01-14 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=14, null=True, verbose_name='Phone Number'),
        ),
    ]
