# Generated by Django 3.2.11 on 2022-02-09 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Informations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Information',
        ),
    ]
