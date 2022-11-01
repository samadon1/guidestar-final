# Generated by Django 4.1.2 on 2022-11-01 09:29

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('checked', models.BooleanField(default=False, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactus_title', models.TextField(blank=True, null=True)),
                ('contactus_subtitle', models.TextField(blank=True, null=True)),
                ('contactus_image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Csv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='media/csvs/')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('activated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landing_title', models.TextField(blank=True, null=True)),
                ('landing_subtitle', models.TextField(blank=True, null=True)),
                ('landing_image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('features_title', models.TextField(blank=True, null=True)),
                ('first_feature_image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('first_feature_title', models.TextField(blank=True, null=True)),
                ('first_feature_subtitle', models.TextField(blank=True, null=True)),
                ('second_feature_image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('second_feature_title', models.TextField(blank=True, null=True)),
                ('second_feature_subtitle', models.TextField(blank=True, null=True)),
                ('third_feature_image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('third_feature_title', models.TextField(blank=True, null=True)),
                ('third_feature_subtitle', models.TextField(blank=True, null=True)),
                ('value_title', models.TextField(blank=True, null=True)),
                ('value_image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('first_value_title', models.TextField(blank=True, null=True)),
                ('first_value_subtitle', models.TextField(blank=True, null=True)),
                ('second_value_title', models.TextField(blank=True, null=True)),
                ('second_value_subtitle', models.TextField(blank=True, null=True)),
                ('third_value_title', models.TextField(blank=True, null=True)),
                ('third_value_subtitle', models.TextField(blank=True, null=True)),
                ('banner_title', models.TextField(blank=True, null=True)),
                ('quote_decription_title', models.TextField(blank=True, null=True)),
                ('quote_decription_subtitle', models.TextField(blank=True, null=True)),
                ('quote_title', models.TextField(blank=True, null=True)),
                ('quote_name', models.TextField(blank=True, null=True)),
                ('quote_position', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ngo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=200)),
                ('principal_officer', models.CharField(max_length=200, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=40, null=True, region=None)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('contact_person', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=500, null=True)),
                ('EIN', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('profile_picture', models.ImageField(blank=True, max_length=200, null=True, upload_to='media/images/')),
                ('checked', models.BooleanField(default=False, verbose_name='Non profit staff')),
                ('verified', models.BooleanField(default=False)),
                ('request', models.BooleanField(default=False)),
                ('compliance_doc', models.FileField(blank=True, null=True, upload_to='media/doc/')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.category')),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='NonProfits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nonprofits_title', models.TextField(blank=True, null=True)),
                ('nonprofits_subtitle', models.TextField(blank=True, null=True)),
                ('nonprofits_image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('nonprofits_work_title', models.TextField(blank=True, null=True)),
                ('nonprofits_work_subtitle', models.TextField(blank=True, null=True)),
                ('first_nonprofit_title', models.TextField(blank=True, null=True)),
                ('first_nonprofit_subtitle', models.TextField(blank=True, null=True)),
                ('second_nonprofit_title', models.TextField(blank=True, null=True)),
                ('second_nonprofit_subtitle', models.TextField(blank=True, null=True)),
                ('third_nonprofit_title', models.TextField(blank=True, null=True)),
                ('third_nonprofit_subtitle', models.TextField(blank=True, null=True)),
                ('fourth_nonprofit_title', models.TextField(blank=True, null=True)),
                ('fourth_nonprofit_subtitle', models.TextField(blank=True, null=True)),
                ('partnerships_title', models.TextField(blank=True, null=True)),
                ('partnerships_subtitle', models.TextField(blank=True, null=True)),
                ('first_partnerships_title', models.TextField(blank=True, null=True)),
                ('first_partnerships_subtitle', models.TextField(blank=True, null=True)),
                ('second_partnerships_title', models.TextField(blank=True, null=True)),
                ('second_partnerships_subtitle', models.TextField(blank=True, null=True)),
                ('nonprofits_banner_title', models.TextField(blank=True, null=True)),
                ('nonprofits_banner_subtitle', models.TextField(blank=True, null=True)),
                ('first_banner_list', models.TextField(blank=True, null=True)),
                ('second_banner_list', models.TextField(blank=True, null=True)),
                ('third_banner_list', models.TextField(blank=True, null=True)),
                ('fourth_banner_list', models.TextField(blank=True, null=True)),
                ('first_banner_list_title', models.TextField(blank=True, null=True)),
                ('first_banner_list_subtitle', models.TextField(blank=True, null=True)),
                ('second_banner_list_title', models.TextField(blank=True, null=True)),
                ('second_banner_list_subtitle', models.TextField(blank=True, null=True)),
                ('third_banner_list_title', models.TextField(blank=True, null=True)),
                ('third_banner_list_subtitle', models.TextField(blank=True, null=True)),
                ('fourth_banner_list_title', models.TextField(blank=True, null=True)),
                ('fourth_banner_list_subtitle', models.TextField(blank=True, null=True)),
                ('nonprofits_cover_image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partners_title', models.TextField(blank=True, null=True)),
                ('patners_subtitle', models.TextField(blank=True, null=True)),
                ('patners_image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('partners_benefit_title', models.TextField(blank=True, null=True)),
                ('partners_benefit_subtitle', models.TextField(blank=True, null=True)),
                ('first_benefit_title', models.TextField(blank=True, null=True)),
                ('first_benefit_subtitle', models.TextField(blank=True, null=True)),
                ('second_benefit_title', models.TextField(blank=True, null=True)),
                ('second_benefit_subtitle', models.TextField(blank=True, null=True)),
                ('third_benefit_title', models.TextField(blank=True, null=True)),
                ('third_benefit_subtitle', models.TextField(blank=True, null=True)),
                ('fourth_benefit_title', models.TextField(blank=True, null=True)),
                ('fourth_benefit_subtitle', models.TextField(blank=True, null=True)),
                ('ways_title', models.TextField(blank=True, null=True)),
                ('ways_subtitle', models.TextField(blank=True, null=True)),
                ('first_ways_image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('first_ways_title', models.TextField(blank=True, null=True)),
                ('second_ways_image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('second_ways_title', models.TextField(blank=True, null=True)),
                ('third_ways_image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('third_ways_title', models.TextField(blank=True, null=True)),
                ('process_image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('process_title', models.TextField(blank=True, null=True)),
                ('process_subtitle', models.TextField(blank=True, null=True)),
                ('first_process_title', models.TextField(blank=True, null=True)),
                ('first_process_subtitle', models.TextField(blank=True, null=True)),
                ('second_process_title', models.TextField(blank=True, null=True)),
                ('second_process_subtitle', models.TextField(blank=True, null=True)),
                ('partners_cover_image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_support_headline', models.TextField(blank=True, null=True)),
                ('first_support_description', models.TextField(blank=True, null=True)),
                ('second_support_headline', models.TextField(blank=True, null=True)),
                ('second_support_description', models.TextField(blank=True, null=True)),
                ('third_support_headline', models.TextField(blank=True, null=True)),
                ('third_support_description', models.TextField(blank=True, null=True)),
                ('fourth_support_headline', models.TextField(blank=True, null=True)),
                ('fourth_support_description', models.TextField(blank=True, null=True)),
                ('ngo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.ngo')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('user_type', models.CharField(choices=[('D', 'Donor'), ('S', 'Supporter'), ('P', 'Partner')], default='D', max_length=2)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField()),
                ('ngo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.ngo')),
            ],
        ),
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_program_image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('first_program_headline', models.TextField(blank=True, null=True)),
                ('first_program_description', models.TextField(blank=True, null=True)),
                ('second_program_image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('second_program_headline', models.TextField(blank=True, null=True)),
                ('second_program_description', models.TextField(blank=True, null=True)),
                ('third_program_image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('third_program_headline', models.TextField(blank=True, null=True)),
                ('third_program_description', models.TextField(blank=True, null=True)),
                ('ngo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.ngo')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_page_image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('second_page_image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('general_description', models.TextField(blank=True, null=True)),
                ('our_mission', models.TextField(blank=True, null=True)),
                ('our_programs', models.TextField(blank=True, null=True)),
                ('our_impact', models.TextField(blank=True, null=True)),
                ('support_us', models.TextField(blank=True, null=True)),
                ('donation', models.TextField(blank=True, null=True)),
                ('ngo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.ngo')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('your_name', models.CharField(blank=True, max_length=200)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=40, null=True, region=None)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ngo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.ngo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Impact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_impact_headline', models.TextField(blank=True, null=True)),
                ('first_impact_description', models.TextField(blank=True, null=True)),
                ('second_impact_headline', models.TextField(blank=True, null=True)),
                ('second_impact_description', models.TextField(blank=True, null=True)),
                ('third_impact_headline', models.TextField(blank=True, null=True)),
                ('third_impact_description', models.TextField(blank=True, null=True)),
                ('ngo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.ngo')),
            ],
        ),
        migrations.CreateModel(
            name='DonationUse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_donation_image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('first_donation_description', models.TextField(blank=True, null=True)),
                ('second_donation_image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('second_donation_description', models.TextField(blank=True, null=True)),
                ('third_donation_image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('third_donation_description', models.TextField(blank=True, null=True)),
                ('fourth_donation_image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('fourth_donation_description', models.TextField(blank=True, null=True)),
                ('ngo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.ngo')),
            ],
        ),
        migrations.CreateModel(
            name='DonationInstruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_account_name', models.CharField(blank=True, max_length=200, null=True)),
                ('bank_account_number', models.CharField(blank=True, max_length=200, null=True)),
                ('momo_name', models.CharField(blank=True, max_length=200, null=True)),
                ('momo_number', models.CharField(blank=True, max_length=200, null=True)),
                ('ngo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.ngo')),
            ],
        ),
        migrations.CreateModel(
            name='ClaimProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=200)),
                ('role', models.TextField(blank=True, max_length=200, verbose_name='Briefly describe your role ')),
                ('connection', models.CharField(choices=[('Staff', 'Staff'), ('Board member', 'Board member'), ('Volunteer', 'Volunteer'), ('Consultant', 'Consultant')], default='Staff', max_length=20, verbose_name='How are you connected to the organization?')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=40, region=None)),
                ('email_address', models.EmailField(blank=True, max_length=254)),
                ('organization_website', models.URLField(blank=True)),
                ('location', models.CharField(blank=True, max_length=500)),
                ('compliance_doc', models.FileField(blank=True, upload_to='media/doc/')),
                ('accept', models.BooleanField(default=False)),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('ngo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.ngo')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('blog_title', models.TextField(blank=True, null=True)),
                ('blog_subtitle', models.TextField(blank=True, null=True)),
                ('blog_image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('blog_content', ckeditor.fields.RichTextField()),
                ('ngo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.ngo')),
            ],
        ),
    ]
