# Generated by Django 5.0.4 on 2024-04-26 05:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_status', models.IntegerField(choices=[(1, 'Live'), (0, 'Delete')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner', to='customers.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.IntegerField(choices=[(2, 'ORDER_PROCESSED'), (3, 'ORDER_DELIVERED'), (4, 'ORDER_REJECTED')], default=0)),
                ('quantity', models.IntegerField(default=1)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_item', to='orders.order')),
                ('products', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='add_cart', to='products.products')),
            ],
        ),
    ]
