# Generated by Django 4.1.4 on 2022-12-25 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src_med', '0002_carrer_alter_contact_phn_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrer',
            name='job_role',
            field=models.CharField(choices=[('1', 'Others'), ('2', 'Technician'), ('3', 'Designer')], default='1', max_length=20),
        ),
    ]
