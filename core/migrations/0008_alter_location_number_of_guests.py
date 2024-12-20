# Generated by Django 5.1.2 on 2024-12-11 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_location_location_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='number_of_guests',
            field=models.CharField(blank=True, choices=[('2-6', '2 to 6'), ('7-15', '7 to 15'), ('16-30', '16 to 30'), ('30-50', '30 to 50')], max_length=10, null=True),
        ),
    ]
