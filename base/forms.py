from dataclasses import field
from distutils.command.config import config
from pyexpat import model
from statistics import mode
from django import forms
from django.forms import ModelForm
from .models import Blog, ClaimProfile, ContactUs, Csv, Homepage, Impact, Ngo, NonProfits, Page,Category, DonationInstruction, Partners, Programs, DonationUse, Support, Reviews
# from .models import 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextFormField 


class RegisterUserForm(UserCreationForm):
    email_address = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField( max_length=70 ,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField( max_length=70,widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField( max_length=70 ,widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label= "Enter password", max_length=70 ,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label= "Confirm password", max_length=70 ,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    checked = forms.BooleanField(required=False, label='Non profit staff')




    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email_address','password1','password2','checked')





class NgoForm(ModelForm):
    class Meta:
        model = Ngo
        fields = '__all__' 
        exclude = ['host', 'verified', 'request', 'checked']

        widgets = {
            'category': forms.Select(attrs={'class':'form-control'}),
            'organization_name':forms.TextInput(attrs={'class':'form-control'}),
            'principal_officer':forms.TextInput(attrs={'class':'form-control'}),
            'contact_person':forms.TextInput(attrs={'class':'form-control'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control'}),
            'email_address':forms.EmailInput(attrs={'class':'form-control'}),
            'website':forms.TextInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'EIN':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'profile_picture':forms.FileInput(),
            'compliance_doc':forms.FileInput(),

        }

        # Todo
        # Multiple ngos belonging to a particulat host

class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = '__all__'
        exclude = ['user', 'ngo', 'date']

        widgets = {
            'user_type' :forms.Select(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'comment': forms.Textarea(attrs={'class':'form-control'})
        }

class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = '__all__' 
        exclude = ['ngo']
        # fields = ('general_description','our_mission','our_programs','our_impact', 'support_us'  )

        widgets = {
            'general_description':forms.Textarea(attrs={'class':'form-control'}),
            'first_page_image':forms.FileInput(),
            'second_page_image':forms.FileInput(),
            'our_mission':forms.Textarea(attrs={'class':'form-control'}),
            'our_programs':forms.Textarea(attrs={'class':'form-control'}),
            'our_impact':forms.Textarea(attrs={'class':'form-control'}),
            'support_us':forms.Textarea(attrs={'class':'form-control'}),
            'donation':forms.Textarea(attrs={'class':'form-control'}),


        }

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ProgramsForm(ModelForm):
    class Meta:
        model = Programs
        fields = '__all__'
        exclude = ['ngo']

        widgets = {
            
            'first_program_image':forms.FileInput(),
            'first_program_headline':forms.TextInput(attrs={'class':'form-control'}),
            'first_program_description':forms.TextInput(attrs={'class':'form-control'}),


            'second_program_image':forms.FileInput(),
            'second_program_headline':forms.TextInput(attrs={'class':'form-control'}),
            'second_program_description':forms.TextInput(attrs={'class':'form-control'}),


            'third_program_image':forms.FileInput(),
            'third_program_headline':forms.TextInput(attrs={'class':'form-control'}),
            'third_program_description':forms.TextInput(attrs={'class':'form-control'}),
        }

class ImpactForm(ModelForm):
    class Meta:
        model = Impact
        fields = '__all__'
        exclude = ['ngo']

        widgets = {
            'first_impact_headline':forms.TextInput(attrs={'class':'form-control'}),
            'first_impact_description':forms.TextInput(attrs={'class':'form-control'}),

            'second_impact_headline':forms.TextInput(attrs={'class':'form-control'}),
            'second_impact_description':forms.TextInput(attrs={'class':'form-control'}),

            'third_impact_headline':forms.TextInput(attrs={'class':'form-control'}),
            'third_impact_description':forms.TextInput(attrs={'class':'form-control'}),
        }

class SupportForm(ModelForm):
    class Meta:
        model = Support
        fields = '__all__'
        exclude = ['ngo']

        widgets = {
            'first_support_headline':forms.TextInput(attrs={'class':'form-control'}),
            'first_support_description':forms.TextInput(attrs={'class':'form-control'}),

            'second_support_headline':forms.TextInput(attrs={'class':'form-control'}),
            'second_support_description':forms.TextInput(attrs={'class':'form-control'}),

            'third_support_headline':forms.TextInput(attrs={'class':'form-control'}),
            'third_support_description':forms.TextInput(attrs={'class':'form-control'}),

            'fourth_support_headline':forms.TextInput(attrs={'class':'form-control'}),
            'fourth_support_description':forms.TextInput(attrs={'class':'form-control'}),
        }

class DonationUseForm(ModelForm):
    class Meta:
        model = DonationUse
        fields = '__all__'
        exclude = ['ngo']

        widgets = {
            
            'first_donation_image':forms.FileInput(),
            'first_donation_description':forms.TextInput(attrs={'class':'form-control'}),

            'second_donation_image':forms.FileInput(),
            'second_donation_description':forms.TextInput(attrs={'class':'form-control'}),

            'third_donation_image':forms.FileInput(),
            'third_donation_description':forms.TextInput(attrs={'class':'form-control'}),

            'fourth_donation_image':forms.FileInput(),
            'fourth_donation_description':forms.TextInput(attrs={'class':'form-control'}),
        }

class DonationInstructionForm(ModelForm):
    class Meta:
        model = DonationInstruction
        fields = ('bank_account_name','bank_account_number','momo_name','momo_number')

        widgets = {
            
            'bank_account_name':forms.TextInput(attrs={'class':'form-control'}),
            'bank_account_number':forms.TextInput(attrs={'class':'form-control'}),
            'momo_name':forms.TextInput(attrs={'class':'form-control'}),
            'momo_number':forms.TextInput(attrs={'class':'form-control'}),
        }


class NonProfitsForm(ModelForm):
    class Meta:
        model = NonProfits
        fields = '__all__'

        widgets = {
            'nonprofits_title':forms.TextInput(attrs={'class':'form-control'}),
            'nonprofits_subtitle':forms.TextInput(attrs={'class':'form-control'}),
            'nonprofits_image':forms.FileInput(),

            'nonprofits_work_title':forms.TextInput(attrs={'class':'form-control'}),
            'nonprofits_work_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            'first_nonprofit_title':forms.TextInput(attrs={'class':'form-control'}),
            'first_nonprofit_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            'second_nonprofit_title':forms.TextInput(attrs={'class':'form-control'}),
            'second_nonprofit_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            
            'third_nonprofit_title':forms.TextInput(attrs={'class':'form-control'}),
            'third_nonprofit_subtitle':forms.TextInput(attrs={'class':'form-control'}),
            
            
            'fourth_nonprofit_title':forms.TextInput(attrs={'class':'form-control'}),
            'fourth_nonprofit_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            'partnerships_title':forms.TextInput(attrs={'class':'form-control'}),
            'partnerships_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            'first_partnerships_title':forms.TextInput(attrs={'class':'form-control'}),
            'first_partnerships_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            'second_partnerships_title':forms.TextInput(attrs={'class':'form-control'}),
            'second_partnerships_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            'nonprofits_banner_title':forms.TextInput(attrs={'class':'form-control'}),
            'nonprofits_banner_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            'first_banner_list':forms.TextInput(attrs={'class':'form-control'}),
            'second_banner_list':forms.TextInput(attrs={'class':'form-control'}),
            'third_banner_list':forms.TextInput(attrs={'class':'form-control'}),
            'fourth_banner_list':forms.TextInput(attrs={'class':'form-control'}),

            'first_banner_list_title':forms.TextInput(attrs={'class':'form-control'}),
            'first_banner_list_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            'second_banner_list_title':forms.TextInput(attrs={'class':'form-control'}),
            'second_banner_list_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            'third_banner_list_title':forms.TextInput(attrs={'class':'form-control'}),
            'third_banner_list_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            'fourth_banner_list_title':forms.TextInput(attrs={'class':'form-control'}),
            'fourth_banner_list_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            'nonprofits_cover_image':forms.FileInput(),

            
        }

class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

        widgets = {
            'contactus_title':forms.TextInput(attrs={'class':'form-control'}),
            'contactus_subtitle':forms.TextInput(attrs={'class':'form-control'}),
            'contactus_image':forms.FileInput(),
            }


class PartnersForm(ModelForm):
    class Meta:
        model = Partners
        fields = '__all__'

        widgets = {
            'partners_title':forms.TextInput(attrs={'class':'form-control'}),
            'patners_subtitle':forms.TextInput(attrs={'class':'form-control'}),
            'patners_image':forms.FileInput(),

            'partners_benefit_title':forms.TextInput(attrs={'class':'form-control'}),
            'partners_benefit_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            'first_benefit_title':forms.TextInput(attrs={'class':'form-control'}),
            'first_benefit_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            'second_benefit_title':forms.TextInput(attrs={'class':'form-control'}),
            'second_benefit_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            'third_benefit_title':forms.TextInput(attrs={'class':'form-control'}),
            'third_benefit_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            'fourth_benefit_title':forms.TextInput(attrs={'class':'form-control'}),
            'fourth_benefit_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            'ways_title':forms.TextInput(attrs={'class':'form-control'}),
            'ways_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            'first_ways_image':forms.TextInput(attrs={'class':'form-control'}),
            'first_ways_title':forms.TextInput(attrs={'class':'form-control'}),

            'second_ways_image':forms.TextInput(attrs={'class':'form-control'}),
            'second_ways_title':forms.TextInput(attrs={'class':'form-control'}),

            'third_ways_image':forms.TextInput(attrs={'class':'form-control'}),
            'third_ways_title':forms.TextInput(attrs={'class':'form-control'}),

            'process_image':forms.FileInput(),
            'process_title':forms.TextInput(attrs={'class':'form-control'}),
            'process_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            'first_process_title':forms.TextInput(attrs={'class':'form-control'}),
            'first_process_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            'second_process_title':forms.TextInput(attrs={'class':'form-control'}),
            'second_process_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            'partners_cover_image':forms.FileInput(),


        }



class HomePageForm(ModelForm):
    class Meta:
        model = Homepage
        fields = '__all__'

        widgets = {
            
            'landing_title':forms.TextInput(attrs={'class':'form-control'}),
            'landing_subtitle':forms.TextInput(attrs={'class':'form-control'}),
            'landing_image':forms.FileInput(),

            'features_title':forms.TextInput(attrs={'class':'form-control'}),
            'first_feature_image':forms.FileInput(),
            'first_feature_title':forms.TextInput(attrs={'class':'form-control'}),
            'first_feature_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            
            'second_feature_image':forms.FileInput(),
            'second_feature_title':forms.TextInput(attrs={'class':'form-control'}),
            'second_feature_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            'third_feature_image':forms.FileInput(),
            'third_feature_title':forms.TextInput(attrs={'class':'form-control'}),
            'third_feature_subtitle':forms.TextInput(attrs={'class':'form-control'}),
            
            'value_title':forms.TextInput(attrs={'class':'form-control'}),
            'value_image':forms.FileInput(),

            'first_value_title':forms.TextInput(attrs={'class':'form-control'}),
            'first_value_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            'second_value_title':forms.TextInput(attrs={'class':'form-control'}),
            'second_value_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            'third_value_title':forms.TextInput(attrs={'class':'form-control'}),
            'third_value_subtitle':forms.TextInput(attrs={'class':'form-control'}),
            
            'banner_title':forms.TextInput(attrs={'class':'form-control'}),

            'quote_decription_title':forms.TextInput(attrs={'class':'form-control'}),
            'quote_decription_subtitle':forms.TextInput(attrs={'class':'form-control'}),

            'quote_title':forms.TextInput(attrs={'class':'form-control'}),
            'quote_name':forms.TextInput(attrs={'class':'form-control'}),
            'quote_position':forms.TextInput(attrs={'class':'form-control'}),
        }


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        exclude = ['ngo']
        fields = '__all__'

        widgets = {
            
            'blog_title':forms.TextInput(attrs={'class':'form-control'}),
            'blog_subtitle':forms.TextInput(attrs={'class':'form-control'}),
            'blog_image':forms.FileInput(),
            'blog_content': RichTextFormField()
        
        }


class CsvModelForm(ModelForm):
    class Meta:
        model = Csv
        fields = ('file_name',)

class ClaimProfileForm(ModelForm):
    class Meta:
        model = ClaimProfile
        exclude = ['ngo', 'accept', 'host']
        fields = '__all__'

        widgets = {
            
            'full_name':forms.TextInput(attrs={'class':'form-control'}),
            # 'connection':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'email_address':forms.EmailInput(attrs={'class':'form-control'}),
            'organization_website':forms.TextInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'organization_website':forms.TextInput(attrs={'class':'form-control'}),
            'role':forms.Textarea(attrs={'class':'form-control'}),
            'compliance_doc':forms.FileInput(),
        
        }