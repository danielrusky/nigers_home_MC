# Generated by Django 4.2.6 on 2023-10-24 11:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0003_alter_category_description_alter_product_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]
