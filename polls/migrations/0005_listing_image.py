# Generated by Django 2.0.7 on 2018-08-08 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_type_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.CharField(default='', max_length=500),
        ),
    ]
