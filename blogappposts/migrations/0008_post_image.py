# Generated by Django 4.1.7 on 2023-03-27 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogappposts', '0007_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]