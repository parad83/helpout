# Generated by Django 4.0.3 on 2022-10-19 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0022_alter_post_id_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.CharField(default='DGVLGRK9Jq', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]