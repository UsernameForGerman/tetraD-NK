# Generated by Django 3.0.9 on 2020-08-08 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0005_auto_20200808_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(db_index=True, max_length=256, unique=True)),
            ],
        ),
    ]
