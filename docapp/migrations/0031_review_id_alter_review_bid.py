# Generated by Django 4.2.5 on 2023-10-30 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docapp', '0030_remove_review_id_alter_review_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='bid',
            field=models.IntegerField(null=True),
        ),
    ]
