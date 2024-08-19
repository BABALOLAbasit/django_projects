# Generated by Django 3.0.3 on 2024-08-10 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('daily_savings', models.IntegerField()),
                ('loan_collected', models.IntegerField()),
                ('remark', models.CharField(max_length=100)),
            ],
        ),
    ]
