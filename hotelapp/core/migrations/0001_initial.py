# Generated by Django 5.1.4 on 2024-12-23 15:23

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='OurRooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='profile', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jfif'])])),
                ('content', models.CharField(max_length=200)),
                ('star_rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.rating')),
            ],
        ),
    ]
