# Generated by Django 5.0.3 on 2024-04-06 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='DateTime',
            new_name='datetime',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Issue',
            new_name='issue',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Phone',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='SNO',
            new_name='s_no',
        ),
    ]
