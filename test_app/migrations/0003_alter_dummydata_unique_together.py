# Generated by Django 5.1.4 on 2025-01-01 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_alter_dummydata_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='dummydata',
            unique_together={('first_name', 'last_name')},
        ),
    ]