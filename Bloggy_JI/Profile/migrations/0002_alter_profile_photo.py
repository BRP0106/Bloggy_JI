# Generated by Django 5.0.1 on 2024-03-22 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default=True, upload_to='Profile_Photo/'),
        ),
    ]