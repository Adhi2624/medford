# Generated by Django 4.1.4 on 2023-01-03 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src_med', '0005_remove_carrer_job_role_carrer_message_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrer',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
    ]