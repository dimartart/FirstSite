# Generated by Django 4.2.3 on 2023-11-13 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifeplan', '0010_alter_order_client_mail_alter_order_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinorder',
            name='size_of_product',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
