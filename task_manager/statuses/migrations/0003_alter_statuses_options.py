# Generated by Django 4.1.4 on 2022-12-25 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0002_alter_statuses_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statuses',
            options={'ordering': ['id'], 'verbose_name': 'Status', 'verbose_name_plural': 'Statuses'},
        ),
    ]
