# Generated by Django 3.1.2 on 2020-10-24 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kegiatanku', '0003_auto_20201024_1143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='peserta',
            old_name='sesuatu',
            new_name='kegiatan',
        ),
    ]