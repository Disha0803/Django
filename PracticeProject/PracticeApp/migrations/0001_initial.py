# Generated by Django 3.2.11 on 2022-03-17 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField()),
                ('cname', models.CharField(max_length=30)),
                ('ccost', models.FloatField()),
            ],
        ),
    ]
