# Generated by Django 4.2 on 2024-01-20 13:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_pic",
            field=models.ImageField(
                default="../default-avatar_qvwzg2", upload_to="images/"
            ),
        ),
    ]
