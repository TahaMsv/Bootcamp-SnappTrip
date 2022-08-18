# Generated by Django 4.1 on 2022-08-18 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('action_id', models.IntegerField(primary_key=True, serialize=False)),
                ('fixedDisplaymentAmount', models.DecimalField(decimal_places=0, max_digits=20)),
                ('percentageDisplaymentAmount', models.DecimalField(decimal_places=0, max_digits=20)),
                ('maximumDisplaymentAmount', models.DecimalField(decimal_places=0, max_digits=20)),
            ],
        ),
    ]