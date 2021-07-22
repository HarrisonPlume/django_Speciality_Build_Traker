# Generated by Django 3.2.5 on 2021-07-21 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0061_componentpreptaskinstance_createtime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='componentpreptaskinstance',
            name='totaltime',
        ),
        migrations.AddField(
            model_name='componentpreptaskinstance',
            name='createtimenum',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True),
        ),
        migrations.AddField(
            model_name='componentpreptaskinstance',
            name='starttimenum',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True),
        ),
        migrations.AddField(
            model_name='componentpreptaskinstance',
            name='timetaken',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True),
        ),
        migrations.AddField(
            model_name='componentpreptaskinstance',
            name='timetostartnum',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True),
        ),
    ]
