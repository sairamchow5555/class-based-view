# Generated by Django 4.1.7 on 2023-05-04 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('taste', models.CharField(max_length=100)),
                ('colour', models.CharField(max_length=100)),
                ('price', models.FloatField()),
            ],
        ),
    ]
