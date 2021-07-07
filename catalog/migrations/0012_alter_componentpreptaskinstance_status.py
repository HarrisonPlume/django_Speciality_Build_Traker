# Generated by Django 3.2.5 on 2021-07-07 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_part_cptasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componentpreptaskinstance',
            name='status',
            field=models.CharField(choices=[('a', 'Not Started'), ('h', 'On Hold'), ('c', 'Complete'), ('p', 'In Progress'), ('f', 'Failed')], default='a', help_text='Book                                   availability', max_length=1),
        ),
    ]
