# Generated by Django 3.1.6 on 2021-02-05 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createaccount',
            name='accno',
            field=models.IntegerField(max_length=15, unique=True),
        ),
    ]
