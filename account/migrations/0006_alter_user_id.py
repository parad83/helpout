# Generated by Django 4.0.3 on 2022-10-23 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='8651357443', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]