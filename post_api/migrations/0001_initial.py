# Generated by Django 5.0.2 on 2024-02-24 16:13

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'posts',
            },
        ),
    ]
