# Generated by Django 4.1.5 on 2023-01-21 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='../static/file'),
        ),
    ]
