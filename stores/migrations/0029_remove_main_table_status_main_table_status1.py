# Generated by Django 5.2 on 2025-05-25 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0028_main_table_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main_table',
            name='Status',
        ),
        migrations.AddField(
            model_name='main_table',
            name='Status1',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='stores.status'),
        ),
    ]
