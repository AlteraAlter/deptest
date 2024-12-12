# Generated by Django 5.1.2 on 2024-12-11 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_location_location_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='location',
            name='location_type',
            field=models.CharField(blank=True, choices=[('CC', 'City Center'), ('MV', 'Mountain View'), ('SV', 'Sea View')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='number_of_guests',
            field=models.CharField(blank=True, choices=[('2-6', '2 to 6'), ('30-50', '30 to 50'), ('7-15', '7 to 15'), ('16-30', '16 to 30')], max_length=10, null=True),
        ),
    ]
