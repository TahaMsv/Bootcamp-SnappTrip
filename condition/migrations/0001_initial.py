# Generated by Django 4.1 on 2022-08-18 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('condiotion', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=255)),
                ('operator', models.CharField(max_length=7)),
                ('value', models.CharField(max_length=255)),
            ],
        ),
    ]
