# Generated by Django 3.1.2 on 2020-10-21 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendrier', '0006_auto_20201020_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='types',
            name='nom',
            field=models.CharField(choices=[(30, 'Simple'), (45, 'Spécialisé'), (55, 'Manipulation')], default=30, max_length=2),
        ),
    ]
