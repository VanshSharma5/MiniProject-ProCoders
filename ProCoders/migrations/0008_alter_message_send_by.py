# Generated by Django 5.1.3 on 2024-12-12 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProCoders', '0007_room_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='send_by',
            field=models.CharField(max_length=128),
        ),
    ]
