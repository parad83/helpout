# Generated by Django 4.0.3 on 2022-10-22 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0032_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='area',
            field=models.CharField(default='Cała Polska', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.CharField(default='A59iuLWkiA', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/2022/10/22'),
        ),
    ]
