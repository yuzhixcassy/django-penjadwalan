# Generated by Django 2.2.12 on 2023-03-03 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penjadwalan', '0022_auto_20230303_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dosen',
            name='nip',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dosen',
            name='notelp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]