# Generated by Django 4.2.5 on 2023-10-30 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docapp', '0029_review_remove_appointment_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='id',
        ),
        migrations.AlterField(
            model_name='review',
            name='bid',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]