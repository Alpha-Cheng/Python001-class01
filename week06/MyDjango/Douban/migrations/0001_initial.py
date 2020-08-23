# Generated by Django 2.2.13 on 2020-08-23 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='T1',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('n_star', models.IntegerField()),
                ('short', models.CharField(max_length=400)),
                ('sentiment', models.FloatField()),
            ],
            options={
                'db_table': 't1',
                'managed': False,
            },
        ),
    ]
