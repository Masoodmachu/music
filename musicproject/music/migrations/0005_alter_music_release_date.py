# Generated by Django 5.0.6 on 2024-06-28 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_remove_customuser_date_of_birth_customuser_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='release_date',
            field=models.CharField(max_length=35),
        ),
    ]
