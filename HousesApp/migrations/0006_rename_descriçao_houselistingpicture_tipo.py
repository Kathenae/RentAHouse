# Generated by Django 3.2.5 on 2021-07-22 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HousesApp', '0005_alter_houselistingpicture_descriçao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='houselistingpicture',
            old_name='descriçao',
            new_name='tipo',
        ),
    ]
