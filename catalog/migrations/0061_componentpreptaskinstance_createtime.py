# Generated by Django 3.2.5 on 2021-07-21 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0060_auto_20210721_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='componentpreptaskinstance',
            name='createtime',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
