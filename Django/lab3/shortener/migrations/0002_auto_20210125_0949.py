# Generated by Django 3.1.5 on 2021-01-25 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshort',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]