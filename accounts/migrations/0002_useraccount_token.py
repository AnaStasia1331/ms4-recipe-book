# Generated by Django 3.2.8 on 2021-11-08 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='token',
            field=models.CharField(max_length=50),
        ),
    ]
