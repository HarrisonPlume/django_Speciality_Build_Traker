# Generated by Django 3.2.5 on 2021-07-07 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_alter_part_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
