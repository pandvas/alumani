# Generated by Django 3.1.6 on 2021-08-30 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_eventpoll'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentPassword',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('studentid', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
