# Generated by Django 4.1.2 on 2022-11-01 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='user_type',
            field=models.CharField(choices=[('Donor', 'Donor'), ('Supporter', 'Supporter'), ('Partner', 'Partner')], default='D', max_length=10),
        ),
    ]
