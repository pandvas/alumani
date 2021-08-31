# Generated by Django 3.1.6 on 2021-08-30 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventpoll',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('interested', models.BooleanField(default=True)),
                ('eventid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.event')),
                ('studentid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.student')),
            ],
        ),
    ]
