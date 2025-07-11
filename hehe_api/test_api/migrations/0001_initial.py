# Generated by Django 5.2.1 on 2025-05-22 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('isbn', models.CharField(max_length=20)),
                ('published_date', models.DateField()),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to='covers/')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/')),
            ],
        ),
    ]
