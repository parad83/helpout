# Generated by Django 4.0.3 on 2022-10-06 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.CharField(default='4EZ5rMkhwK', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
