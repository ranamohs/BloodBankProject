# Generated by Django 4.0.3 on 2022-06-17 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodApp', '0002_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('donor_blood', models.CharField(max_length=2)),
                ('The_State', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=14)),
                ('Another_Phone', models.CharField(max_length=14)),
                ('Gender', models.CharField(max_length=6)),
                ('Anychronicdiseases', models.CharField(max_length=3)),
                ('Getting_Dentist_Recently', models.CharField(max_length=3)),
            ],
        ),
    ]
