# Generated by Django 4.1.2 on 2022-11-01 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claimprofile',
            name='connection',
            field=models.CharField(choices=[('Staff', 'Staff'), ('Board member', 'Board member'), ('Volunteer', 'Volunteer'), ('Consultant', 'Consultant')], default='Staff', max_length=25, verbose_name='How are you connected to the organization?'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='user_type',
            field=models.CharField(choices=[('Donor', 'Donor'), ('Supporter', 'Supporter'), ('Partner', 'Partner')], default='Donor', max_length=25),
        ),
    ]
