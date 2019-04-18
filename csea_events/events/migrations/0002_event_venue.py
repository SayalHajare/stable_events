# Generated by Django 2.2 on 2019-04-17 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.CharField(choices=[('L1', 'Lecture Hall 1'), ('L2', 'Lecture Hall 2'), ('L1', 'Lecture Hall 3'), ('L1', 'Lecture Hall 4'), ('Audi', 'Auditorium')], default='Audi', max_length=50),
        ),
    ]