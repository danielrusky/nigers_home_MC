# Generated by Django 4.2.6 on 2023-11-05 06:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0005_version_product_vers"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="vers",
        ),
    ]