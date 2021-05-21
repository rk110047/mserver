# Generated by Django 3.0 on 2020-04-12 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RadioCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('background_image', models.FileField(blank=True, null=True, upload_to='')),
                ('is_adult', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Radio Categories',
            },
        ),
        migrations.CreateModel(
            name='RadioChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('channel_url', models.URLField(max_length=255)),
                ('channel_image', models.FileField(upload_to='')),
                ('EPG_file', models.FileField(blank=True, null=True, upload_to='')),
                ('description', models.TextField()),
                ('is_popular', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(related_name='radio_category', to='radio.RadioCategory')),
            ],
            options={
                'verbose_name_plural': 'Radio Channels',
            },
        ),
    ]
