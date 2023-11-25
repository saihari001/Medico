# Generated by Django 4.2.5 on 2023-10-26 14:34

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('docapp', '0015_alter_appointment_pprescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='bid',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', editable=False, length=4, max_length=4, prefix=''),
        ),
    ]