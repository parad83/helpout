# Generated by Django 4.0.3 on 2022-10-03 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_polandcities_id_alter_post_id_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polandcities',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.CharField(default='5Ys6SAUJii', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
