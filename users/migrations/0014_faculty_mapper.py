# Generated by Django 3.1.6 on 2021-08-30 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_department_mapper'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty_mapper',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('departmentid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.department')),
                ('facultyid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.faculty')),
                ('universityid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.university')),
            ],
        ),
    ]
