# Generated by Django 3.1.2 on 2020-10-22 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendrier', '0016_auto_20201022_1042'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Types',
        ),
        migrations.RemoveField(
            model_name='rdv',
            name='types',
        ),
        migrations.AddField(
            model_name='rdv',
            name='typess',
            field=models.IntegerField(choices=[(30, 'Simple'), (55, 'Manipulation'), (45, 'Spécialisé')], default=30),
        ),
    ]
