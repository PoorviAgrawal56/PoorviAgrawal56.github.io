# Generated by Django 3.1.4 on 2020-12-26 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_photoresume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoresume',
            name='my_photo',
            field=models.ImageField(upload_to='portfolio/personal_files'),
        ),
    ]
