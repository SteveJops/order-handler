# Generated by Django 4.2.4 on 2023-08-27 17:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ordersapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("1", "New"),
                    ("2", "Placed"),
                    ("3", "Given"),
                    ("4", "Refusal"),
                ],
                default="New",
                max_length=10,
            ),
        ),
    ]
