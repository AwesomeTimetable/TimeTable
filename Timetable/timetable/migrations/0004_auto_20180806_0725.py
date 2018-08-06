# Generated by Django 2.0.4 on 2018-08-06 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0003_auto_20180524_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deadline',
            name='ddl_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='timetable.LargeDeadline'),
        ),
        migrations.AlterField(
            model_name='deadline',
            name='tags',
            field=models.ManyToManyField(blank=True, to='timetable.Tag'),
        ),
    ]
