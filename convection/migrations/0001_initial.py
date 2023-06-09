# Generated by Django 4.1.1 on 2023-04-29 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NaturalConvection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.CharField(max_length=10)),
                ('voltage', models.CharField(max_length=10)),
                ('power', models.CharField(max_length=10)),
                ('Temperature_2', models.CharField(max_length=10)),
                ('Temperature_3', models.CharField(max_length=10)),
                ('Temperature_4', models.CharField(max_length=10)),
                ('Temperature_5', models.CharField(max_length=10)),
                ('Temperature_6', models.CharField(max_length=10)),
                ('Ambient_Temperature', models.CharField(max_length=10)),
                ('predicted_output', models.CharField(max_length=10)),
            ],
        ),
    ]
