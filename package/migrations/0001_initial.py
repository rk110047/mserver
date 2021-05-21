# Generated by Django 3.0 on 2020-04-12 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('liveTv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('backgroundImage_url', models.URLField(max_length=255)),
                ('thumbnailImage_url', models.URLField(max_length=255)),
                ('price', models.IntegerField()),
                ('validity', models.DurationField()),
                ('discount', models.IntegerField()),
                ('channel', models.ManyToManyField(to='liveTv.Channels')),
            ],
            options={
                'verbose_name_plural': 'Packages',
            },
        ),
    ]