# Generated by Django 3.2.9 on 2022-06-25 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220625_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
