# Generated by Django 4.1.7 on 2023-04-19 01:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_oder_order_rename_oderitem_orderitem_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='date_order',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='date_order',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='mobile',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
