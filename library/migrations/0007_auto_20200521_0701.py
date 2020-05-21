# Generated by Django 3.0.6 on 2020-05-21 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20200521_0623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='author',
            name='first_name',
            field=models.CharField(default='Jack', max_length=30),
        ),
        migrations.AddField(
            model_name='author',
            name='second_name',
            field=models.CharField(default='London', max_length=30),
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='library.Author'),
        ),
    ]
