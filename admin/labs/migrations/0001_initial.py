# Generated by Django 3.1.3 on 2023-04-27 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Labs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('experiments', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=200)),
            ],
        ),
    ]
