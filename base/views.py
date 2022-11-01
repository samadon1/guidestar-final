#Import neccessary libraries

from cProfile import Profile
import email
from importlib.resources import Resource
from multiprocessing import context
import os
from unicodedata import name
from urllib import response
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, FileResponse
from .models import Blog, ClaimProfile, ContactUs, Csv, DonationInstruction, DonationUse, Homepage, Impact, Ngo , Category, NonProfits, Page, Partners, Programs, Support, Reviews
from .forms import BlogForm, ClaimProfileForm, ContactUsForm, CsvModelForm, DonationInstructionForm, DonationUseForm, HomePageForm, ImpactForm, NgoForm, NonProfitsForm, PartnersForm, ProgramsForm, RegisterUserForm , PageForm, CategoryForm, ReviewForm, SupportForm
from multiselectfield import MultiSelectField
from django.urls import reverse
import stripe
from. filters import CategoryFilter
from django.contrib import messages 
import csv






# Create your views here.
@login_required(login_url = 'login')    
def update_donation(request, pk):
    ngo = Ngo.objects.get(id=pk)
    donation_instruction = DonationInstruction.objects.filter(ngo = ngo).first()
    form = DonationInstructionForm(instance = donation_instruction)

    if request.user != ngo.host:
        return HttpResponse("You can't do this here!!")

    if request.method == 'POST':
        form = DonationInstructionForm(request.POST, instance = donation_instruction)
        if form.is_valid():
            form.save()
            return redirect('home')

    context= {'form': form}
    return render(request, 'base/donation_form.html',context)


def donation_instruction(request, pk):
    ngo = Ngo.objects.get(id=pk)
    donation_instruction = DonationInstruction.objects.filter(ngo = ngo).first()
    if donation_instruction is None:
        donation_instruction = DonationInstruction.objects.create(ngo = ngo)

    context = {"donation_instruction": donation_instruction, 'ngo':ngo, }
    return render(request, 'base/donation_instruction.html', context)



def homepage(request):
    return render(request, 'base/homepage.html')

def login_page(request):
    page = 'login'
    msg = False

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username =  request.POST.get('username').lower()
        password =  request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            # messages.error(request, 'User does not exist')
            msg = True

        user = authenticate(request, username = username , password = password)

        if user is not None:
            login (request,user)
            return redirect ('/')
            
        
        else:
            # messages.error(request, 'Username or password does not exist')
            msg = True


    context = {'page':page, 'msg': msg}
    return render(request, 'base/login_register.html', context)


def logout_user(request):
    logout(request)
    messages.error(request, 'Logged out ')
    return redirect('login')

def register_user(request):
    submitted = False
    form = RegisterUserForm()
    
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
       
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            print(form.cleaned_data.get('checked'))
            if form.cleaned_data.get('checked')=='on':
                return redirect('/join_us')
            else:
                return redirect('home')
        
        else:
            messages.error(request, 'An error occurred during registration' )

    else:
        form =RegisterUserForm()
        if 'submitted' in request.GET:
            submitted= True
    
    context = {'form1':form,'submitted':submitted}

    return render(request, 'base/login_register.html', context)


def alert(request):
    form = CategoryForm
    c = filter(request.GET,queryset=Category.objects.all())
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            tt = form.save(commit=False)
            data = form.cleaned_data
            field = data['checked']=True
            c.qs.filter(checked=field).update(checked=True, checkedUser=request.user)
            return HttpResponse('ok')
    else:
        context = {
            'filter': c,
            'form': form
        }
    return render(request, 'home.html',context)

@login_required(login_url = 'login')
def reviews(request, pk):
    ngo = Ngo.objects.get(id=pk)
    form = ReviewForm()


    if request.method == 'POST':
        form = ReviewForm(request.POST)
        form.instance.ngo = ngo
        if form.is_valid():
            form.save()
            return redirect('home')

    context= {'form': form}
    return render(request, 'base/new_review.html',context)

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    
    ngos = Ngo.objects.filter(
        Q(category__name__icontains=q) |
        Q(organization_name__icontains=q) |
        Q(description__icontains=q)|
        Q(location__icontains=q)
        

    ) 
    # ngos = ngos.filter(verified = True)
    # ngos = ngos.filter(verified = True)
    # ngos = ngos.filter(
    #     Q(verified = True)

    # )
    categories = Category.objects.all()
    filters=[]

    if request.method == "GET":
        filters = request.GET.getlist("checkbox")
        ngos = Ngo.objects.filter(
            category__name__in=filters)
        if len(filters) == 0:
            ngos = Ngo.objects.filter(
                Q(category__name__icontains=q) |
                Q(organization_name__icontains=q) |
                Q(description__icontains=q)|
                Q(location__icontains=q) 
                # Q(verified = True)
            )
            # ngos = ngos.filter(verified = True)
        ngo_count = ngos.count()
        return render(request, 'base/home.html', {'ngos': ngos, 'filters': filters, 'categories': categories, 'ngo_count': ngo_count})
    
    else:
        my_filter = CategoryFilter(request.GET, queryset=ngos)
        ngos = my_filter.qs
        

        ngo_count = ngos.count()
        

        context = {'ngos': ngos, 'categories': categories,'ngo_count': ngo_count ,'my_filter':my_filter, "filters":filters}
        return render(request, 'base/home.html', context)

def ngo(request,pk):
    ngo = Ngo.objects.filter(id=pk).first()
    suggestions = Ngo.objects.filter().order_by('?')[:3]
    
    

    blog = Blog.objects.filter(ngo = pk).order_by("-created_on") [:3]
    page = Page.objects.filter(ngo = ngo).first()
    programs = Programs.objects.filter(ngo = ngo).first()
    impact = Impact.objects.filter(ngo=ngo).first()
    support = Support.objects.filter(ngo=ngo).first()
    donation = DonationUse.objects.filter(ngo=ngo).first()
    review = Reviews.objects.filter(ngo=pk)
    
    
# if page is None:
    #     return render(request, 'base/ngo_page_error.html')
    # else:
        

    context = {'review': review, 'ngo':ngo,'page':page, 'programs': programs, 'impact': impact, 
        'support': support, 'donation': donation, "suggestions": suggestions,
        'blog': blog
         }
    return render(request, 'base/profile.html', context)


        


def on_item_select(name):
    print("===== Name=====", name)
    

def about_us(request):
    return render(request, 'base/about_us.html')

@login_required(login_url = 'login')
def join_us(request):
    submitted = False
    form = NgoForm()
    if request.method == 'POST':
        form = NgoForm(request.POST, request.FILES)
        if form.is_valid():
            ngo=form.save(commit=False)
            ngo.host= request.user
            ngo.save()
            return HttpResponseRedirect('/join_us?submitted=True')
    else:
        form = NgoForm()
        if 'submitted' in request.GET:
            submitted= True

    return render(request, 'base/join_us.html', {'form': form ,'submitted':submitted})



@login_required(login_url = 'login')
def create_ngo(request):
    form = NgoForm(request.POST)
    if request.method == 'POST':
        form = NgoForm(request.POST)
        if form.is_valid():
            ngo=form.save(commit=False)
            ngo.host= request.user
            ngo.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/ngo_form.html', context)

#update views

@login_required(login_url = 'login')
def update_homepage(request):

    
    

    try:
        home = Homepage.objects.filter()[:1].get()
    except:
        home =  Homepage.objects.create()

    

    form = HomePageForm(instance=home)
    


    if not request.user.is_superuser:
        return HttpResponse("You can't do this here!!")

    if request.method == 'POST':
        form = HomePageForm(request.POST, request.FILES, instance=home) 
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context= {'form': form}
    return render(request, 'base/update_homepage.html',context)


@login_required(login_url = 'login')
def update_contactus(request):

    
    

    try :
        contactus = ContactUs.objects.filter()[:1].get()
    except:
        contactus =  ContactUs.objects.create()

    

    form = ContactUsForm(instance=contactus)
    


    if not request.user.is_superuser:
        return HttpResponse("You can't do this here!!")

    if request.method == 'POST':
        form = ContactUsForm(request.POST, request.FILES, instance=contactus) 
        if form.is_valid():
            form.save()
            return redirect('contact_us')
    
    context= {'form': form}
    return render(request, 'base/update_contactus.html',context)

@login_required(login_url = 'login')
def update_partners(request):

    
    

    try :
        partners = Partners.objects.filter()[:1].get()
    except:
        partners =  Partners.objects.create()

    

    form = PartnersForm(instance=partners)
    


    # if request.user != ngo.host:
    #     return HttpResponse("You can't do this here!!")

    if request.method == 'POST':
        form = PartnersForm(request.POST, request.FILES, instance=partners) 
        if form.is_valid():
            form.save()
            return redirect('partners')
    
    context= {'form': form}
    return render(request, 'base/update_partners.html',context)

@login_required(login_url = 'login')
def update_resources(request):

    
    

    try :
        nonprofits = NonProfits.objects.filter()[:1].get()
    except:
        nonprofits =  NonProfits.objects.create()

    

    form = NonProfitsForm(instance=nonprofits)
    


    # if request.user != ngo.host:
    #     return HttpResponse("You can't do this here!!")

    if request.method == 'POST':
        form = NonProfitsForm(request.POST, request.FILES, instance=nonprofits) 
        if form.is_valid():
            form.save()
            return redirect('resources')
    
    context= {'form': form}
    return render(request, 'base/update_resources.html',context)

@login_required(login_url = 'login')
def show_pdf(request, pk):
    ngo = Ngo.objects.get(id=pk)
    file = str(ngo.compliance_doc)
    try:
        response = FileResponse(open('uploads/' + file, 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=mypdf.pdf'
        return response
    except FileNotFoundError:
        raise Http404()
    # with open('uploads/media/doc/note1209.txt', 'r', encoding="utf8") as pdf:
    #     # response = HttpResponse(pdf.read(), mimetype='application/pdf')
    #     response['Content-Disposition'] = 'inline;filename=some_file.pdf'
    #     return response
    # pdf.closed

@login_required(login_url= 'login')
def pending(request):
    ngos = Ngo.objects.filter(verified = False)
    context = {'ngos': ngos}
    return render(request, 'base/pending.html', context)

@login_required(login_url= 'login')
def verified(request):
    ngos = Ngo.objects.filter(verified = True)
    context = {'ngos': ngos}
    return render(request, 'base/verified.html', context)

@login_required(login_url = 'login')
def update_ngo(request, pk):
    ngo = Ngo.objects.get(id=pk)
    try:
        page = Page.objects.filter(ngo = ngo).first()
        programs = Programs.objects.filter(ngo = ngo).first()
        impact = Impact.objects.filter(ngo=ngo).first()
        support = Support.objects.filter(ngo=ngo).first()
        donation = DonationUse.objects.filter(ngo=ngo).first()
        donation_instruction = DonationInstruction.objects.filter(ngo = ngo).first()
    except programs.DoesNotExist :
        return None
        # programs = Programs.objects.create(ngo=ngo)
        # impact = Impact.objects.create(ngo=ngo)
        # support = Support.objects.create(ngo=ngo)
        # donation= DonationUse.objects.create(ngo=ngo)
    
    
    form = NgoForm(instance=ngo)
    pageForm = PageForm(instance=page)
    programsForm = ProgramsForm(instance=programs)
    ImpactFormPage = ImpactForm(instance = impact)
    SupportFormPage = SupportForm(instance = support)
    DonationUseFormPage = DonationUseForm(instance=donation)
    DoInstruction = DonationInstructionForm(request.POST, 
        instance = donation_instruction
        )


    if not (page or impact or support or donation or programs)  :
        impact = Impact.objects.create(ngo=ngo)
        support = Support.objects.create(ngo=ngo)
        donation = DonationUse.objects.create(ngo=ngo)
        programs = Programs.objects.create(ngo=ngo)
        page = Page.objects.create(ngo = ngo)
    


    # if request.user != ngo.host or request.is_superuser:
    if not request.user.is_superuser:
        return HttpResponse("You can't do this here!!")

    if request.method == 'POST':
        form = NgoForm(request.POST, request.FILES, instance = ngo )
        programs = ProgramsForm(request.POST, request.FILES, instance=programs)
        support = SupportForm(request.POST, request.FILES, instance=support)
        donation = DonationUseForm(request.POST, request.FILES, instance=donation)
        impact = ImpactForm(request.POST, request.FILES, instance=impact)
        page = PageForm(request.POST, request.FILES, instance = page)
        donInstruction = DonationInstructionForm(request.POST, instance=donation_instruction)
        if form.is_valid() and DoInstruction and programs.is_valid() and support.is_valid() and impact.is_valid() and donation.is_valid():
            donation.save()
            programs.save()
            support.save()
            impact.save()
            form.save()
            page.save()
            donInstruction.save()
            
            return redirect('home')

    context= {'form': form, 'ngo':ngo, 'page': pageForm, 'programs': programsForm, 'impactForm':ImpactFormPage, 
    'supportForm': SupportFormPage, 'donationForm': DonationUseFormPage, 
    'instruction' : DoInstruction
    }
    return render(request, 'base/ngo_form.html',context)




@login_required(login_url = 'login')
def delete_blog(request,pk):

    blog = Blog.objects.get(id = pk)
    

    if not request.user.is_superuser:
        return HttpResponse("You can't do this here!!")

    blog.delete()
    
    return redirect('home')

@login_required(login_url = 'login')
def update_blog(request, pk):
    blog = Blog.objects.get(id = pk)
    form = BlogForm(
        instance = blog
        )

    if not request.user.is_superuser:
        return HttpResponse("You can't do this here!!")

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, 
        instance = blog
        )
        if form.is_valid():
            form.save()
            return redirect('home')

    context= {'form': form}
    return render(request, 'base/new_blog.html',context)




@login_required(login_url = 'login')
def all_blogs(request, pk):
    ngo = Ngo.objects.get(id=pk)
    blog = Blog.objects.filter(ngo = pk).order_by("-created_on") 


    context= {'blogs': blog, 'ngo': ngo}
    return render(request, 'base/all_blogs.html', context)


@login_required(login_url = 'login')
def new_blog(request, pk):
    ngo = Ngo.objects.get(id=pk)
    form = BlogForm()

    if request.user != ngo.host:
        return HttpResponse("You can't do this here!!")

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        form.instance.ngo = ngo
        if form.is_valid():
            form.save()
            return redirect('home')

    context= {'form': form}
    return render(request, 'base/new_blog.html',context)

def blog(request, pk):
    blog = Blog.objects.get(id = pk)
    ngo = Ngo.objects.get(id=blog.ngo.pk)
    


    context= {'form': blog, 'ngo': ngo}
    return render(request, 'base/blog_details.html',context)




@login_required(login_url = 'login')
def create_page(request, pk):
    ngo = Ngo.objects.get(id=pk)
    form = PageForm(instance=ngo)

    if request.user != ngo.host:
        return HttpResponse("You can't do this here!!")

    if request.method == 'POST':
        form = PageForm(request.POST, instance = ngo)
        if form.is_valid():
            form.save()
            return redirect('home')

    context= {'form': form}
    return render(request, 'base/create_form.html',context)



@login_required(login_url = 'login')
def edit_page(request, pk):
    submitted = False
    ngo = Ngo.objects.get(id=pk)
    page = Page.objects.get(ngo = ngo)
    form = PageForm(instance=page)

    if request.user != ngo.host:
        return HttpResponse("You can't do this here!!")

    if request.method == 'POST':
        form = PageForm(request.POST, instance = page)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home?submitted=True')
    
    else:
        form = PageForm(instance=page)
        if submitted in request.GET:
            submitted = True


    context= {'form': form, 'submitted':submitted, 'ngo':ngo}
    return render(request, 'base/edit_form.html',context)





@login_required(login_url = 'login')
def delete_ngo(request,pk):
    ngo = Ngo.objects.get(id=pk)

    if request.user != ngo.host:
        return HttpResponse("You can't do this here!!")

    # if request.method == 'POST':
    
    ngo.delete()
    
    return redirect('home')

    # return render(request, 'base/delete.html', {'obj':ngo})






@login_required(login_url = 'login')
def user_profile(request):
    # ngo = Ngo.objects.get(id)
    user = request.user
    ngos = user.ngo_set.all()

    all_ngos = Ngo.objects.all()

    verification_count = Ngo.objects.filter(request = True).count()
    claim_count = ClaimProfile.objects.filter(accept = False).count()

    context ={'user':user , 'ngos':ngos, 'all_ngos': all_ngos,
     'verification_count':verification_count,
     'claim_count': claim_count
     }
    return render(request, 'base/user_profile.html',context)







def index(request):

    try:
        form = Homepage.objects.filter()[:1].get()
    except:
        form =  Homepage.objects.create()

    # form = Homepage.objects.filter()[:1].get()

    context = {
        "form" : form
    }
    return render(request, 'base/index.html', context)



def contact_us(request):
    return render(request, 'base/contact_us.html')

def resources(request):
    return render(request, 'base/resources.html')

def partners(request):
    return render(request, 'base/partners.html')

def supporters(request):
    return render(request, 'base/supporters.html')

stripe.api_key = "sk_test_51LN8jkB8LrPQL82nvnmXrop74tyv9jMBdbjIekukYmoewDcrRjUirTG9CtZfOE07o2NfPmzHl5vfRKU0OOpM4ux500vTPQUGS6"

def donations(request):
    user = request.user
    ngos = user.ngo_set.all()
    context={'ngos':ngos}
    return render(request, 'base/donations.html',context)

def charge(request):
    
    if request.method == 'POST':
        print('Data:',request.POST)

        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['name'],
            source=request.POST['stripeToken']
            )

        charge = stripe.Charge.create(
			customer = customer,
			amount = amount*100,
			currency='usd',
			description="Donation"
			)
    
        return redirect(reverse('success_msg',args=[amount]))

def success_msg(request,args):
    amount = args
    return render (request, 'base/success_msg.html',{'amount':amount})


@login_required(login_url = 'login')
def claim_profile(request, pk):
    ngo = Ngo.objects.get(id=pk)
    form = ClaimProfileForm()

    if request.method == 'POST':
        form = ClaimProfileForm(request.POST, request.FILES,)
        if form.is_valid():
            # form = form(ngo = ngo, data = request.POST)
            profile=form.save(commit=False)
            profile.ngo  = ngo
            # form = form(ngo = ngo, data = request.POST)
            profile.save()
            return redirect('home')
        else:
            print(form.errors.as_data())
    

    return render(request, 'base/claim_profile_form.html', {'form': form})


def all_claim_request(request):
    claim_profiles = ClaimProfile.objects.filter(accept = False)

    verification_count = Ngo.objects.filter(request = True).count()
    claim_count = ClaimProfile.objects.filter(accept = False).count()
    return render(request, 'base/all_claim_request.html', {"claim_profiles": claim_profiles,
    'verification_count': verification_count,
    'claim_count': claim_count,
    })


def accept_claim(request, email_address):
    # ngo = Ngo.objects.filter(ngo = pk).first()

    profile = ClaimProfile.objects.filter(email_address = email_address).first()
    profile.accept = True

    try:
        profile.host = User.objects.get(email__exact=email_address)
    except:
        return HttpResponse("User does not exist")
   



    profile_ngo = profile.ngo.id
    ngo = Ngo.objects.get(id = profile_ngo)
    ngo.host = User.objects.get(email__exact=email_address)
    ngo.save()
    profile.save()

    return redirect('all_claim_request')
    
def delete_claim(request, pk):
    profile = ClaimProfile.objects.get(id = pk)
    profile.delete()

    return redirect('all_claim_request')


def verification(request):
    verification_count = Ngo.objects.filter(request = True).count()
    claim_count = ClaimProfile.objects.filter(accept = False).count()


    ngos = Ngo.objects.filter(request = True)
    return render(request, 'base/verification_page.html', {'ngos': ngos,
    'verification_count': verification_count,
    'claim_count': claim_count
    })
    


def verification_request(request, pk):
    ngo = Ngo.objects.get(id = pk)
    ngo.request = True
    ngo.save()

    return redirect('home')

def confirm_verification(request,pk):
    ngo = Ngo.objects.get(id = pk)
    ngo.verified = True
    ngo.request = False
    ngo.save()

    return redirect('home')


def upload_file_view(request):
    form = CsvModelForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        form = CsvModelForm()

        obj = Csv.objects.get(activated = False)
        obj.activated = True
        obj.save()
        with open(obj.file_name.path, 'r', encoding='utf-8', errors='ignore') as f:
            reader = csv.reader(f)

            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    # row = "".join(row)
                    # row = row.replace(",", " ")
                    # row = row.split()
                    # print(row)
                    # print(type(row))
                    organization_name = row[0]
                    description = row[1]
                    category = row[2]
                    profile_picture = row[3]


                    new_cat = Category(name = category)
                    if not Category.objects.filter(name = category):
                        new_cat.save()
                    else:
                        new_cat = Category.objects.filter(name = category).first()

                    

                    Ngo.objects.create(
                        organization_name = organization_name,
                        description = description,
                        profile_picture = profile_picture,
                        category = new_cat
                    )

                    
                    

            

    return render(request, 'base/upload_csv.html', {'form': form})