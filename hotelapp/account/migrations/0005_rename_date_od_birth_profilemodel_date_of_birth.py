# Generated by Django 5.1.4 on 2024-12-27 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_profilemodel_date_od_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilemodel',
            old_name='date_od_birth',
            new_name='date_of_birth',
        ),
    ]
