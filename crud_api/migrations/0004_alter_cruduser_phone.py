# Generated by Django 4.2.1 on 2023-05-12 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crud_api", "0003_alter_cruduser_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cruduser",
            name="phone",
            field=models.CharField(blank=True, max_length=10),
        ),
    ]