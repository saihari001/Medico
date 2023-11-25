# Generated by Django 4.2.5 on 2023-10-30 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docapp', '0031_review_id_alter_review_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='id',
        ),
        migrations.AlterField(
            model_name='review',
            name='bid',
            field=models.IntegerField(blank=True, default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]