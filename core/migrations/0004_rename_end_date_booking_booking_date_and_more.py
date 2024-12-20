# Generated by Django 5.1.2 on 2024-12-10 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_date_order_created_at_order_total_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='end_date',
            new_name='booking_date',
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('location', 'booking_date')},
        ),
        migrations.AlterField(
            model_name='location',
            name='location_type',
            field=models.CharField(blank=True, choices=[('MV', 'Mountain View'), ('SV', 'Sea View'), ('CC', 'City Center')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='number_of_guests',
            field=models.CharField(blank=True, choices=[('2-6', '2 to 6'), ('7-15', '7 to 15'), ('30-50', '30 to 50'), ('16-30', '16 to 30')], max_length=10, null=True),
        ),
        migrations.RemoveField(
            model_name='booking',
            name='start_date',
        ),
    ]
