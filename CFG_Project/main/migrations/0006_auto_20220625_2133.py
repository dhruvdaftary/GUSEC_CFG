# Generated by Django 3.2.9 on 2022-06-25 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_user_info_filled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Account_No_Bank',
            field=models.PositiveIntegerField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Funding_requirements',
            field=models.PositiveIntegerField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Funding_status',
            field=models.BooleanField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Name_of_bank',
            field=models.PositiveIntegerField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='PAN',
            field=models.PositiveIntegerField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='founders_email',
            field=models.EmailField(blank=True, max_length=2000, null=True),
        ),
    ]
