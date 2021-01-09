# Generated by Django 3.1.4 on 2020-12-26 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_remove_project_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoResume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_photo', models.ImageField(upload_to='portfolio/images')),
                ('resume', models.URLField(blank=True)),
            ],
        ),
    ]