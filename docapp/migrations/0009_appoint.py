# Generated by Django 4.2.5 on 2023-10-22 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docapp', '0008_imagegallery_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('astatus', models.CharField(default='Pending', max_length=30)),
            ],
        ),
    ]