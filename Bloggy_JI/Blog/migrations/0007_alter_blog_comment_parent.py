# Generated by Django 5.0.1 on 2024-03-28 01:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_alter_blog_comment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_comment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Blog.blog_comment'),
        ),
    ]