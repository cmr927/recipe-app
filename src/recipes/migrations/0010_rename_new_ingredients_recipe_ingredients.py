# Generated by Django 5.1.4 on 2025-02-13 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0009_recipe_new_ingredients"),
    ]

    operations = [
        migrations.RenameField(
            model_name="recipe",
            old_name="new_ingredients",
            new_name="ingredients",
        ),
    ]
