from cProfile import label
from distutils.command.upload import upload
from email.policy import default
from fileinput import FileInput
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField 

# Create your models here.




class Category(models.Model):
    name = models.CharField(max_length=200)
    checked = models.BooleanField(verbose_name='', default=False)

    def __str__(self):
        return self.name


class Ngo(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    organization_name = models.CharField(max_length=200)
    principal_officer = models.CharField(max_length=200, null= True, blank = False)
    contact_person = models.CharField(max_length=200, null= True, blank = True)
    phone_number = PhoneNumberField(max_length=40, null= True, blank = True)
    email_address = models.EmailField(max_length=254 , null= True, blank = True)
    website = models.URLField(max_length=200, null= True, blank = True)
    contact_person = models.CharField(max_length=200, null= True, blank = True)
    location =  models.CharField(max_length=500, null= True, blank = True)
    EIN = models.CharField(max_length=500, null= True, blank = True)
    description = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(null = True, blank = True,upload_to="media/images/")
    checked = models.BooleanField(verbose_name='Non profit staff', default=False)
    verified  = models.BooleanField(default=False)
    request  = models.BooleanField(default=False)
    compliance_doc = models.FileField(upload_to='media/doc/', blank=True, null=True)

    # user_page = models.ForeignKey(Page,on_delete=models.SET_NULL,null=True, blank = True)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add= True)
    # check = models.BooleanField(default=False)


    

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.organization_name
    

class Reviews(models.Model):
    USER_TYPE = (
        ('Donor', 'Donor'),
        ('Supporter', 'Supporter'),
        ('Partner', 'Partner'),
    )
    ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
    name = models.TextField()
    user_type = models.CharField(max_length=25,choices = USER_TYPE, default='Donor')
    date = models.DateTimeField(auto_now_add= True)
    comment = models.TextField()
    
    
    
class Message(models.Model):
    user= models.ForeignKey(User , on_delete=models.CASCADE)
    ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
    body = models.TextField()
    "We'd love to hear from you"
    your_name = models.CharField(max_length=200 , null= False, blank = True)
    email_address = models.EmailField(max_length=254 , null= True, blank = True)
    phone_number = PhoneNumberField(max_length=40, null= True, blank = True)




    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.body



class Page(models.Model):
    ngo = models.ForeignKey(Ngo , on_delete=models.CASCADE)
    first_page_image =  models.ImageField(null = True, blank = True,upload_to="media/images/")
    second_page_image =  models.ImageField(null = True, blank = True,upload_to="media/images/")
    general_description = models.TextField(null=True, blank=True)
    our_mission = models.TextField(null=True, blank=True)
    our_programs = models.TextField(null=True, blank=True)
    our_impact = models.TextField(null=True, blank=True)
    support_us = models.TextField(null=True, blank=True)
    donation = models.TextField(null=True, blank = True)

    def __str__(self):
        return self.general_description

class Programs(models.Model):
    ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
    first_program_image = models.ImageField(null = True, blank = True,upload_to="media/images/")
    first_program_headline = models.TextField(null=True, blank=True)
    first_program_description = models.TextField(null=True, blank=True)


    second_program_image = models.ImageField(null = True, blank = True,upload_to="media/images/")
    second_program_headline = models.TextField(null=True, blank=True)
    second_program_description = models.TextField(null=True, blank=True)


    third_program_image = models.ImageField(null = True, blank = True,upload_to="media/images/")
    third_program_headline = models.TextField(null=True, blank=True)
    third_program_description = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return self.first_program_description

class Impact(models.Model):
    ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
    first_impact_headline = models.TextField(null=True, blank=True)
    first_impact_description = models.TextField(null=True, blank=True)

    second_impact_headline = models.TextField(null=True, blank=True)
    second_impact_description = models.TextField(null=True, blank=True)

    third_impact_headline = models.TextField(null=True, blank=True)
    third_impact_description = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return self.first_impact_description

class Support(models.Model):
    ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
    first_support_headline = models.TextField(null=True, blank=True)
    first_support_description = models.TextField(null=True, blank=True)

    second_support_headline = models.TextField(null=True, blank=True)
    second_support_description = models.TextField(null=True, blank=True)

    third_support_headline = models.TextField(null=True, blank=True)
    third_support_description = models.TextField(null=True, blank=True)

    fourth_support_headline = models.TextField(null=True, blank=True)
    fourth_support_description = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return self.first_support_description

class DonationUse(models.Model):
    ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
    first_donation_image = models.ImageField(null = True, blank = True,upload_to="media/images/")
    first_donation_description = models.TextField(null=True, blank=True)
    second_donation_image = models.ImageField(null = True, blank = True,upload_to="media/images/")
    second_donation_description = models.TextField(null=True, blank=True)
    third_donation_image = models.ImageField(null = True, blank = True,upload_to="media/images/")
    third_donation_description = models.TextField(null=True, blank=True)
    fourth_donation_image = models.ImageField(null = True, blank = True,upload_to="media/images/")
    fourth_donation_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.first_donation_description

class DonationInstruction(models.Model):
    ngo = models.ForeignKey(Ngo , on_delete=models.CASCADE, null=True, blank=True)
    bank_account_name = models.CharField(max_length=200, null=True, blank=True)
    bank_account_number = models.CharField(max_length=200, null=True, blank=True)
    momo_name = models.CharField(max_length=200, null=True, blank=True)
    momo_number = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.bank_account_name

class Homepage(models.Model):
    landing_title = models.TextField(null=True, blank=True)
    landing_subtitle = models.TextField(null=True, blank=True)
    landing_image = models.ImageField(null = True, blank = True,upload_to="media/images/")

    features_title = models.TextField(null=True, blank=True)
    first_feature_image = models.ImageField(null = True, blank = True,upload_to="media/images/")
    first_feature_title = models.TextField(null=True, blank=True)
    first_feature_subtitle = models.TextField(null=True, blank=True)

    second_feature_image = models.ImageField(null = True, blank = True,upload_to="media/images/")
    second_feature_title = models.TextField(null=True, blank=True)
    second_feature_subtitle = models.TextField(null=True, blank=True)

    third_feature_image = models.ImageField(null = True, blank = True,upload_to="media/images/")
    third_feature_title = models.TextField(null=True, blank=True)
    third_feature_subtitle = models.TextField(null=True, blank=True)

    value_title = models.TextField(null=True, blank=True)
    value_image = models.ImageField(null = True, blank = True,upload_to="media/images/")

    first_value_title = models.TextField(null=True, blank=True)
    first_value_subtitle = models.TextField(null=True, blank=True)

    second_value_title = models.TextField(null=True, blank=True)
    second_value_subtitle = models.TextField(null=True, blank=True)

    third_value_title = models.TextField(null=True, blank=True)
    third_value_subtitle = models.TextField(null=True, blank=True)

    banner_title = models.TextField(null=True, blank=True)

    quote_decription_title = models.TextField(null=True, blank=True)
    quote_decription_subtitle = models.TextField(null=True, blank=True)

    quote_title = models.TextField(null=True, blank=True)
    quote_name = models.TextField(null=True, blank=True)
    quote_position = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.landing_title

class ContactUs(models.Model):
    contactus_title = models.TextField(null=True, blank=True)
    contactus_subtitle = models.TextField(null=True, blank=True)
    contactus_image = models.ImageField(null = True, blank = True,upload_to="media/images/")


class NonProfits(models.Model):
    nonprofits_title = models.TextField(null=True, blank=True)
    nonprofits_subtitle = models.TextField(null=True, blank=True)
    nonprofits_image = models.ImageField(null = True, blank = True,upload_to="media/images/")

    nonprofits_work_title = models.TextField(null=True, blank=True)
    nonprofits_work_subtitle = models.TextField(null=True, blank=True)

    first_nonprofit_title =   models.TextField(null=True, blank=True)
    first_nonprofit_subtitle =   models.TextField(null=True, blank=True)

    second_nonprofit_title =   models.TextField(null=True, blank=True)
    second_nonprofit_subtitle =   models.TextField(null=True, blank=True)

    third_nonprofit_title =   models.TextField(null=True, blank=True)
    third_nonprofit_subtitle =   models.TextField(null=True, blank=True)

    fourth_nonprofit_title =   models.TextField(null=True, blank=True)
    fourth_nonprofit_subtitle =   models.TextField(null=True, blank=True)

    partnerships_title = models.TextField(null=True, blank=True)
    partnerships_subtitle = models.TextField(null=True, blank=True)

    first_partnerships_title = models.TextField(null=True, blank=True)
    first_partnerships_subtitle = models.TextField(null=True, blank=True)

    second_partnerships_title = models.TextField(null=True, blank=True)
    second_partnerships_subtitle = models.TextField(null=True, blank=True)

    nonprofits_banner_title = models.TextField(null=True, blank=True)
    nonprofits_banner_subtitle = models.TextField(null=True, blank=True)

    first_banner_list = models.TextField(null=True, blank=True)
    second_banner_list = models.TextField(null=True, blank=True)
    third_banner_list = models.TextField(null=True, blank=True)
    fourth_banner_list = models.TextField(null=True, blank=True)

    first_banner_list_title = models.TextField(null=True, blank=True)
    first_banner_list_subtitle = models.TextField(null=True, blank=True)

    second_banner_list_title = models.TextField(null=True, blank=True)
    second_banner_list_subtitle = models.TextField(null=True, blank=True)

    third_banner_list_title = models.TextField(null=True, blank=True)
    third_banner_list_subtitle = models.TextField(null=True, blank=True)

    fourth_banner_list_title = models.TextField(null=True, blank=True)
    fourth_banner_list_subtitle = models.TextField(null=True, blank=True)


    nonprofits_cover_image = models.ImageField(null = True, blank = True,upload_to="media/images/")
    



class Partners(models.Model):
    partners_title = models.TextField(null=True, blank=True)
    patners_subtitle = models.TextField(null=True, blank=True)
    patners_image = models.ImageField(null = True, blank = True,upload_to="media/images/")

    partners_benefit_title = models.TextField(null=True, blank=True)
    partners_benefit_subtitle = models.TextField(null=True, blank=True)

    first_benefit_title =   models.TextField(null=True, blank=True)
    first_benefit_subtitle =   models.TextField(null=True, blank=True)

    second_benefit_title =   models.TextField(null=True, blank=True)
    second_benefit_subtitle =   models.TextField(null=True, blank=True)

    third_benefit_title =   models.TextField(null=True, blank=True)
    third_benefit_subtitle =   models.TextField(null=True, blank=True)

    fourth_benefit_title =   models.TextField(null=True, blank=True)
    fourth_benefit_subtitle =   models.TextField(null=True, blank=True)

    ways_title = models.TextField(null=True, blank=True)
    ways_subtitle = models.TextField(null=True, blank=True)

    first_ways_image = models.ImageField(null = True, blank = True,upload_to="media/images/")
    first_ways_title = models.TextField(null=True, blank=True)

    second_ways_image = models.ImageField(null = True, blank = True,upload_to="media/images/")
    second_ways_title = models.TextField(null=True, blank=True)

    third_ways_image = models.ImageField(null = True, blank = True,upload_to="media/images/")
    third_ways_title = models.TextField(null=True, blank=True)

    process_image = models.ImageField(null = True, blank = True,upload_to="media/images/")
    process_title = models.TextField(null=True, blank=True)
    process_subtitle = models.TextField(null=True, blank=True)

    first_process_title = models.TextField(null=True, blank=True)
    first_process_subtitle = models.TextField(null=True, blank=True)

    second_process_title = models.TextField(null=True, blank=True)
    second_process_subtitle = models.TextField(null=True, blank=True)

    partners_cover_image = models.ImageField(null = True, blank = True,upload_to="media/images/")

class Blog(models.Model):
    # id = models.AutoField(primary_key=True)
    ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    blog_title = models.TextField(null=True, blank=True)
    blog_subtitle = models.TextField(null=True, blank=True)
    blog_image = models.ImageField(null = True, blank = True,upload_to="media/images/")
    blog_content = RichTextField()

    
class Csv(models.Model):
    file_name = models.FileField(upload_to='media/csvs/')
    uploaded = models.DateTimeField(auto_now_add = True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"


class ClaimProfile(models.Model):
    CONNECTIONS = (
        ('Staff', 'Staff'),
        ('Board member', 'Board member'),
        ('Volunteer', 'Volunteer'),
        ('Consultant', 'Consultant'),
    )
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, null= False, blank = True)
    role = models.TextField(verbose_name="Briefly describe your role ", max_length=200, null= False, blank = True)
    connection = models.CharField(verbose_name="How are you connected to the organization?", max_length=25, choices = CONNECTIONS, default='Staff')
    phone = PhoneNumberField(max_length=40, null= False, blank = True)
    email_address = models.EmailField(max_length=254 , null= False, blank = True)
    organization_website = models.URLField(max_length=200, null= False, blank = True)
    location =  models.CharField(max_length=500, null= False, blank = True)
    compliance_doc = models.FileField(upload_to='media/doc/', blank=True, null=False)
    accept  = models.BooleanField(default=False)
