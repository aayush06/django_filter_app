# Generated by Django 2.1.2 on 2018-10-26 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0005_auto_20181026_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='pg_course',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
