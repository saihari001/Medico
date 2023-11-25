# Generated by Django 4.2.5 on 2023-10-26 14:52

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('docapp', '0017_alter_appointment_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='id',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='bid',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=4, max_length=4, prefix='', primary_key=True, serialize=False),
        ),
    ]