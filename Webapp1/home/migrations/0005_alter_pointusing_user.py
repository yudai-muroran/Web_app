# Generated by Django 4.1.5 on 2023-01-23 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_pointusing_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointusing',
            name='user',
            field=models.CharField(max_length=255),
        ),
    ]