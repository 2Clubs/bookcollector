# Generated by Django 4.2 on 2023-04-28 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_reading_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='date',
            field=models.DateTimeField(verbose_name='reading date'),
        ),
    ]
