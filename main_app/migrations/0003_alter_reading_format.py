# Generated by Django 4.2 on 2023-04-28 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_reading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='format',
            field=models.CharField(choices=[('H', 'Hard Copy'), ('E', 'E-Reader')], default='H', max_length=1),
        ),
    ]
