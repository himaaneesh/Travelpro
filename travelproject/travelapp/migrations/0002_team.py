# Generated by Django 3.2.15 on 2022-10-14 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=250)),
                ('image1', models.ImageField(upload_to='mypics')),
                ('desc1', models.TextField()),
            ],
        ),
    ]
