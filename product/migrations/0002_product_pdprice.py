# Generated by Django 3.2.5 on 2021-07-21 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pdprice',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
