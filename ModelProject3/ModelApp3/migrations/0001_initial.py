# Generated by Django 3.2.11 on 2022-02-01 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
                ('ename', models.CharField(max_length=30)),
                ('eaddr', models.CharField(max_length=40)),
                ('esal', models.FloatField()),
            ],
        ),
    ]
