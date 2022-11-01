# Generated by Django 4.1.2 on 2022-11-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_claimprofile_connection_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='compliance_doc',
            field=models.FileField(blank=True, max_length=2000, null=True, upload_to='media/doc/'),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='profile_picture',
            field=models.ImageField(blank=True, max_length=2000, null=True, upload_to='media/images/'),
        ),
    ]
