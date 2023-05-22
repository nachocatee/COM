# Generated by Django 3.2.6 on 2023-05-22 02:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('listId', models.IntegerField(primary_key=True, serialize=False)),
                ('id', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField(null=True)),
                ('poster_path', models.TextField(null=True)),
                ('release_date', models.DateField(default=datetime.date.today, null=True)),
                ('vote_average', models.FloatField(null=True)),
                ('vote_count', models.IntegerField(null=True)),
            ],
        ),
    ]