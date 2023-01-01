# Generated by Django 4.0.3 on 2022-10-19 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0023_alter_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('1', "I'm looking for help"), ('2', "I'm offering help")], default="I'm looking for help", max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.CharField(default='GxBnrtmFbv', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
