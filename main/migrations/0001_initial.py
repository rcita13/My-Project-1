# Generated by Django 4.2.3 on 2023-08-27 15:11

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('image', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('ingredients', models.TextField()),
                ('directions', models.TextField()),
                ('servings', models.CharField(max_length=5)),
                ('time', models.CharField(max_length=5)),
                ('calories', models.CharField(max_length=5)),
                ('fat', models.CharField(max_length=5)),
                ('carbs', models.CharField(max_length=5)),
                ('protein', models.CharField(max_length=5)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.topic')),
            ],
        ),
    ]
