# Generated by Django 2.2 on 2019-04-17 22:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Btech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('name', models.CharField(max_length=300)),
                ('event_id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular event', primary_key=True, serialize=False)),
                ('fee', models.PositiveIntegerField()),
                ('capacity', models.PositiveIntegerField()),
                ('target_audience', models.CharField(max_length=300)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('summary', models.TextField(blank=True, null=True)),
                ('faq', models.TextField(blank=True, null=True)),
                ('tags', models.CharField(help_text=' (Press Ctrl to select multiple)', max_length=300)),
                ('organisors', models.CharField(max_length=300)),
                ('contact_info', models.CharField(max_length=300)),
                ('comment_for_admin', models.CharField(max_length=300)),
                ('invitees_btech', models.ManyToManyField(help_text=' (Press Ctrl to select multiple)', to='events.Btech')),
            ],
        ),
        migrations.CreateModel(
            name='Mtech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PhD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_coming', models.PositiveIntegerField()),
                ('response_not_coming', models.PositiveIntegerField()),
                ('response_not_sure', models.PositiveIntegerField()),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='invitees_mtech',
            field=models.ManyToManyField(help_text=' (Press Ctrl to select multiple)', to='events.Mtech'),
        ),
        migrations.AddField(
            model_name='event',
            name='invitees_phd',
            field=models.ManyToManyField(to='events.PhD'),
        ),
    ]