# Generated by Django 2.2.5 on 2021-09-07 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EdTech', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='key_features',
            field=models.TextField(max_length=200),
        ),
    ]
