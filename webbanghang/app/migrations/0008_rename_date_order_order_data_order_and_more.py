# Generated by Django 4.1.7 on 2023-05-10 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date_order',
            new_name='data_order',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='date_added',
            new_name='data_added',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='date_order',
            new_name='data_order',
        ),
    ]
