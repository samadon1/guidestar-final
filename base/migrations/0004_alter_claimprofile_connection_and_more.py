# Generated by Django 4.1.2 on 2022-11-01 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_claimprofile_connection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claimprofile',
            name='connection',
            field=models.CharField(choices=[('S', 'S'), ('B', 'B'), ('V', 'V'), ('C', 'C')], default='S', max_length=2, verbose_name='How are you connected to the organization?'),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='organization_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='user_type',
            field=models.CharField(choices=[('D', 'D'), ('S', 'S'), ('P', 'P')], default='D', max_length=2),
        ),
    ]