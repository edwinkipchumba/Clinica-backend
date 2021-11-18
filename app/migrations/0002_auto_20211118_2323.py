# Generated by Django 3.2.7 on 2021-11-18 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emergingdisease',
            name='link',
        ),
        migrations.RemoveField(
            model_name='growth',
            name='link',
        ),
        migrations.RemoveField(
            model_name='vaccine',
            name='category',
        ),
        migrations.RemoveField(
            model_name='vaccine',
            name='link',
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='drug_expiry',
            field=models.DateField(),
        ),
    ]
