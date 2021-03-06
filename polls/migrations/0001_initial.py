# Generated by Django 2.0.7 on 2018-08-06 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('listId', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('lid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('pid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('purpose', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('tid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Location'),
        ),
        migrations.AddField(
            model_name='listing',
            name='purpose',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Purpose'),
        ),
        migrations.AddField(
            model_name='listing',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Type'),
        ),
    ]
