# Generated by Django 3.0.3 on 2020-04-23 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20200422_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]
