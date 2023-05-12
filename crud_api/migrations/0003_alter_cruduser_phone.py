# Generated by Django 4.2.1 on 2023-05-11 12:05

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("crud_api", "0002_alter_cruduser_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cruduser",
            name="phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=128, region=None
            ),
        ),
    ]