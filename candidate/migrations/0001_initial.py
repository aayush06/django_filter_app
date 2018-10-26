# Generated by Django 2.1.2 on 2018-10-25 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=50)),
                ('work_exp', models.FloatField()),
                ('analytics_exp', models.FloatField()),
                ('resume', models.BooleanField(default=True)),
                ('current_loc', models.CharField(max_length=50)),
                ('corrected_loc', models.CharField(max_length=50)),
                ('nearest_loc', models.CharField(max_length=50)),
                ('ctc', models.FloatField()),
                ('current_employer', models.CharField(max_length=50)),
                ('current_desig', models.CharField(max_length=50)),
                ('ug_course', models.CharField(max_length=50)),
                ('ug_institute', models.CharField(max_length=50)),
                ('trier_1', models.CharField(max_length=50)),
                ('ug_pass_year', models.CharField(max_length=50)),
                ('pg_course', models.CharField(max_length=50)),
                ('pg_institute', models.CharField(max_length=50)),
                ('pg_pass_year', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=200)),
                ('skills', models.TextField()),
            ],
        ),
    ]