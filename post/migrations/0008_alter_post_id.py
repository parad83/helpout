# Generated by Django 4.0.3 on 2022-10-05 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_alter_post_area_alter_post_id_alter_post_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.CharField(default='JmfqfM6Spp', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
