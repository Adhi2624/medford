# Generated by Django 4.1.4 on 2022-12-24 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phn_no', models.IntegerField()),
                ('subject', models.CharField(max_length=38)),
                ('email', models.EmailField(max_length=50)),
                ('message', models.TextField(max_length=250)),
            ],
        ),
    ]
