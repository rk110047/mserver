# Generated by Django 3.0 on 2020-08-01 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscription', '0002_auto_20200801_1230'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usersubscriptionpackage',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='usersubscriptionpackage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='usersubscriptionpackage',
            unique_together=set(),
        ),
    ]
