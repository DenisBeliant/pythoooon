# Generated by Django 3.1.2 on 2020-10-22 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendrier', '0017_auto_20201022_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rdv',
            name='typess',
        ),
        migrations.AddField(
            model_name='rdv',
            name='types',
            field=models.IntegerField(choices=[(55, 'Manipulation'), (30, 'Simple'), (45, 'Spécialisé')], default=30),
        ),
    ]
