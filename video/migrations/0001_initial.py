# Generated by Django 4.1.5 on 2023-01-09 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('video_id', models.TextField()),
                ('publish_time', models.TextField()),
                ('description', models.TextField()),
                ('thumbnail', models.TextField()),
            ],
        ),
    ]
