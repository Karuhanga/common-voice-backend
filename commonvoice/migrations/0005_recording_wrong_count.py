# Generated by Django 2.2 on 2019-04-20 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commonvoice', '0004_auto_20190420_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='recording',
            name='wrong_count',
            field=models.IntegerField(default=0),
        ),
    ]
