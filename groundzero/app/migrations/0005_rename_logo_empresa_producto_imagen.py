# Generated by Django 3.2 on 2021-07-04 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='logo_empresa',
            new_name='imagen',
        ),
    ]
