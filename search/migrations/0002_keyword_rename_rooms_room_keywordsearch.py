# Generated by Django 4.0.3 on 2022-03-07 00:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Keyword',
                'verbose_name_plural': 'Keywords',
            },
        ),
        migrations.RenameModel(
            old_name='Rooms',
            new_name='Room',
        ),
        migrations.CreateModel(
            name='KeywordSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=250)),
                ('register_on', models.DateTimeField(auto_now_add=True)),
                ('count', models.IntegerField(blank=True, default=0)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='search_keywords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'KeywordSearch',
                'verbose_name_plural': 'Searching Word',
            },
        ),
    ]
