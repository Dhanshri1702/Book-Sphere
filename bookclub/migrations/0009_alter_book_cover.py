# Generated by Django 4.2.17 on 2024-12-16 21:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bookclub", "0008_alter_book_cover"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="cover",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
