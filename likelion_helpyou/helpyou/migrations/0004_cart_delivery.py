# Generated by Django 4.2 on 2023-08-02 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("helpyou", "0003_alter_categorysmall_categorybig"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="delivery",
            field=models.CharField(default="3000", max_length=30),
        ),
    ]
