# Generated by Django 4.0.3 on 2022-10-19 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0024_post_type_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.CharField(default='HiDU6XsCEH', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(max_length=20),
        ),
    ]
