# Generated by Django 4.0.3 on 2022-11-14 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='4886579475', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]