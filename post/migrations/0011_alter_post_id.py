# Generated by Django 4.0.3 on 2022-10-05 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.CharField(default='BBp2Hkm6Bi', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
