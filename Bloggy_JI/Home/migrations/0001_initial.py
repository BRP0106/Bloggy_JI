# Generated by Django 5.0.1 on 2024-02-21 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('SNO', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Phone', models.CharField(max_length=13)),
                ('Issue', models.TextField()),
                ('DateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]