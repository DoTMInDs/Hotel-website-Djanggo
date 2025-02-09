# Generated by Django 5.1.4 on 2024-12-25 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_ourrooms_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('content', models.TextField(null=True)),
                ('dated_on', models.TimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-dated_on',),
            },
        ),
    ]
