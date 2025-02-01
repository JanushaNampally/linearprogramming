# Generated by Django 5.1 on 2025-01-28 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='linearprogramminginput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=50)),
                ('equations', models.TextField()),
                ('solution', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
