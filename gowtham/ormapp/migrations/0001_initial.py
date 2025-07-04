# Generated by Django 5.1.7 on 2025-04-16 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.CharField(help_text='User ID', max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('person_email', models.EmailField(max_length=254)),
                ('seats', models.IntegerField()),
                ('Movie_Name', models.CharField(max_length=20)),
                ('Show_Date', models.DateTimeField()),
                ('Phone_Number', models.CharField(help_text='Phone number', max_length=10)),
            ],
        ),
    ]
