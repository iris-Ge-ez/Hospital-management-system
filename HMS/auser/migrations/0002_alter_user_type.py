# Generated by Django 4.0.4 on 2022-05-03 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('DR', 'Doctor'), ('NU', 'Nurse'), ('LAB', 'Laboratorist'), ('RT', 'Receptionist'), ('HM', 'Hospital Manager'), ('DI', 'Director'), ('PH', 'Pharmacist')], max_length=50, verbose_name='Type'),
        ),
    ]
