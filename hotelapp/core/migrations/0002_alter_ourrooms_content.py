# Generated by Django 5.1.4 on 2024-12-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourrooms',
            name='content',
            field=models.TextField(null=True),
        ),
    ]