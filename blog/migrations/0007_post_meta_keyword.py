# Generated by Django 3.0.3 on 2020-06-14 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200402_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='meta_keyword',
            field=models.CharField(default='Hello There', max_length=200),
        ),
    ]
