# Generated by Django 4.1.7 on 2023-03-24 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=250)),
                ('yosh', models.IntegerField(blank=True, null=True)),
                ('tugulgan_kun', models.CharField(blank=True, max_length=250, null=True)),
                ('guruh', models.CharField(max_length=250)),
                ('tel_raqam', models.CharField(max_length=250)),
            ],
        ),
    ]
