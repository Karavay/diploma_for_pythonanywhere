# Generated by Django 3.0.7 on 2021-04-30 18:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='id')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, verbose_name='second name')),
                ('sex', models.IntegerField(verbose_name='sex')),
                ('status', models.TextField(verbose_name='user status')),
                ('city', models.CharField(max_length=30, verbose_name='city')),
                ('bdate', models.CharField(max_length=15, verbose_name='birth date')),
                ('about', models.TextField(verbose_name='about')),
                ('activities', models.TextField(verbose_name='activities')),
                ('books', models.TextField(verbose_name='books')),
                ('career', models.TextField(verbose_name='career')),
                ('connections', models.TextField(verbose_name='connections')),
                ('contacts', models.TextField(verbose_name='contacts')),
                ('country', models.CharField(max_length=30, verbose_name='country')),
                ('domain', models.CharField(max_length=50, verbose_name='domain')),
                ('education', models.TextField(verbose_name='education')),
                ('home_town', models.CharField(max_length=30, verbose_name='home town')),
                ('received_date', models.DateTimeField(default=datetime.datetime(2021, 4, 30, 18, 30, 3, 963088, tzinfo=utc), verbose_name='time of receiving data')),
            ],
            options={
                'verbose_name': 'единица информации',
                'verbose_name_plural': 'полученные данные',
            },
        ),
    ]
