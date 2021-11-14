# Generated by Django 3.2.7 on 2021-11-14 21:55

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import url_or_relative_url_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('batch_number', models.DecimalField(decimal_places=2, max_digits=12)),
                ('drug_expiry', models.TextField()),
                ('user_profile', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('next_appointment', models.CharField(max_length=50)),
                ('link', url_or_relative_url_field.fields.URLOrRelativeURLField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vaccines', to='app.category')),
                ('vaccine_name', models.ManyToManyField(through='app.Cart', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('profile_pic', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('contact', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Growth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('HO', models.IntegerField()),
                ('date', models.DateField()),
                ('link', url_or_relative_url_field.fields.URLOrRelativeURLField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmergingDisease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_name', models.CharField(max_length=200)),
                ('next_appointment', models.CharField(max_length=50)),
                ('link', url_or_relative_url_field.fields.URLOrRelativeURLField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='vaccine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.vaccine'),
        ),
    ]
