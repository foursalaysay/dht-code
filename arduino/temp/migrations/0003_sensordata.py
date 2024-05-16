# Generated by Django 5.0.5 on 2024-05-15 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0002_rename_user_userdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]