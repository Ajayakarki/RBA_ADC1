# Generated by Django 3.0.1 on 2020-02-09 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback', '0002_feedback_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='img',
            field=models.ImageField(upload_to='shop/'),
        ),
    ]
