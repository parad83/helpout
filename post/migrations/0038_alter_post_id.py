# Generated by Django 4.0.3 on 2022-10-23 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0037_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.CharField(default='u46fsdySQY', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]