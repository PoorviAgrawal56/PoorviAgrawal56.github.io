# Generated by Django 3.1.4 on 2020-12-26 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20201226_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoresume',
            name='resume',
            field=models.FileField(blank=True, upload_to='portfolio/personal_files'),
        ),
    ]