# Generated by Django 3.1.2 on 2020-10-23 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kegiatanku', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daftarpeserta',
            name='sesuatu',
        ),
        migrations.AddField(
            model_name='peserta',
            name='sesuatu',
            field=models.ManyToManyField(to='kegiatanku.tags'),
        ),
    ]
