# Generated by Django 3.0 on 2020-08-30 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
    ]
