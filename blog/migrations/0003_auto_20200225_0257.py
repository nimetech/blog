# Generated by Django 3.0.3 on 2020-02-24 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200225_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='posts', to='blog.Category'),
        ),
    ]
