# Generated by Django 4.2.5 on 2023-10-29 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docapp', '0019_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.AddField(
            model_name='appointment',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]