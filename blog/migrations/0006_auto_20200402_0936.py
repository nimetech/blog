# Generated by Django 3.0.3 on 2020-04-02 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200306_0813'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'get_latest_by': 'created_on', 'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(default='featured_image/none.jpg', upload_to='featured_image'),
        ),
    ]
