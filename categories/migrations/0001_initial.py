# Generated by Django 4.1.5 on 2023-01-05 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.SmallIntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
            ],
        ),
    ]
