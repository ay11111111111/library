# Generated by Django 3.0.6 on 2020-05-20 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_author_num_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100),
        ),
    ]
