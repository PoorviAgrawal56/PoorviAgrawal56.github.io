# Generated by Django 3.1.4 on 2020-12-28 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20201226_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='technology',
            field=models.CharField(default='0000000', max_length=250),
        ),
    ]
