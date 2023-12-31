# Generated by Django 4.2.5 on 2023-10-24 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docapp', '0009_appoint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pfname', models.CharField(max_length=40)),
                ('plname', models.CharField(max_length=40)),
                ('pgender', models.CharField(max_length=10)),
                ('page', models.IntegerField(max_length=3)),
                ('pemail', models.CharField(max_length=100)),
                ('pnumber', models.IntegerField(max_length=10)),
                ('pvisited', models.CharField(max_length=4)),
                ('pspecialist', models.CharField(max_length=30)),
                ('pappiontdate', models.DateField()),
                ('pappionttime', models.TimeField()),
            ],
        ),
    ]
