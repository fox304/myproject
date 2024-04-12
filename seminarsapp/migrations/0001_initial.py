# Generated by Django 5.0.2 on 2024-02-19 06:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.TextField()),
                ('dob', models.DateField()),
                ('fullname', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RandomDrops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side', models.CharField(default='орел', max_length=10)),
                ('time_drop', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('publicated_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(max_length=100)),
                ('view_count', models.IntegerField(default=0)),
                ('publicated_flag', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seminarsapp.authormodel')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('changed_date', models.DateTimeField(auto_now=True)),
                ('publicated_date', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seminarsapp.articlemodel')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seminarsapp.authormodel')),
            ],
        ),
    ]
