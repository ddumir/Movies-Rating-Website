# Generated by Django 4.2.3 on 2023-09-23 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peterpeepshow', '0002_rename_diractor_movies_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='m_hour',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='movies',
            name='m_year',
            field=models.IntegerField(),
        ),
    ]
