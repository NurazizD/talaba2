# Generated by Django 4.1.7 on 2023-03-28 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pii', '0003_rename_url_versiya_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='versiya',
            name='name',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
    ]
