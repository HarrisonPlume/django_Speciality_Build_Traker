# Generated by Django 3.2.5 on 2021-07-08 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0028_team'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['title']},
        ),
    ]
