# Generated by Django 4.0.3 on 2022-10-22 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='8044155016', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]