# Generated by Django 4.2.3 on 2023-09-22 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifeplan', '0002_supply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supply',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='supply',
            name='size',
            field=models.IntegerField(),
        ),
    ]