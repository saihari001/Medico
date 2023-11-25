# Generated by Django 4.2.5 on 2023-10-29 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docapp', '0028_alter_appointment_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('bid', models.IntegerField(blank=True, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='rate',
        ),
    ]
