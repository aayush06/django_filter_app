# Generated by Django 2.1.2 on 2018-10-26 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0002_auto_20181026_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='analytics_exp',
            field=models.FloatField(blank=True),
        ),
    ]
