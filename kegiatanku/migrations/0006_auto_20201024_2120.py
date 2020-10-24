# Generated by Django 3.1.2 on 2020-10-24 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kegiatanku', '0005_auto_20201024_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peserta',
            name='kegiatan',
        ),
        migrations.AddField(
            model_name='tags',
            name='peserta_kegiatan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kegiatanku.peserta'),
        ),
    ]