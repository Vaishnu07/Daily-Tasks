# Generated by Django 4.1.3 on 2022-11-21 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swiggy', '0003_remove_food_ondelete'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='quality',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
