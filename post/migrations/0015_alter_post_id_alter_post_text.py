# Generated by Django 4.0.3 on 2022-10-06 17:36

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.CharField(default='KvRiQM3Fv2', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(max_length=500, validators=[account.models.profanity_filter]),
        ),
    ]
