from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name = 'home'),

    path('', views.index, name = 'index'),

    path('upload_csv/', views.upload_file_view, name = 'upload_csv'),
    path('claim_profile/<str:pk>/', views.claim_profile, name = 'claim_profile'),
    path('all_claim_request/', views.all_claim_request, name = 'all_claim_request'),
    path('accept_claim/<str:email_address>/', views.accept_claim, name = 'accept_claim'),
    path('verification/', views.verification, name = 'verification'),
    path('verification_request/<str:pk>/', views.verification_request, name = 'verification_request'),
    path('confirm_verification/<str:pk>/', views.confirm_verification, name = 'confirm_verification'),
    path('delete_claim/<str:pk>/', views.delete_claim, name = 'delete_claim'),





    path('login/', views.login_page, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('register/', views.register_user, name = 'register'),
    
    
    path('home/', views.home, name = 'home'),
    path('home/<str:pk>/', views.ngo, name = 'ngo'),
    path('ngo_page_error/', views.ngo, name = 'no_ngo'),
    path('about_us/', views.about_us, name = 'about_us'),
    path('join_us/', views.join_us, name = 'join_us'),
    path('contact_us/', views.contact_us, name = 'contact_us'),
    path('resources/', views.resources, name = 'resources'),
    path('partners/', views.partners, name = 'partners'),
    path('supporters/', views.supporters, name = 'supporters'),
    path('homepage/', views.homepage, name = 'homepage'),




    path('create_ngo/',views.create_ngo, name = 'create_ngo'),
    path('show_pdf/<str:pk>',views.show_pdf, name = 'show_pdf'),
    path('update_ngo/<str:pk>/', views.update_ngo, name = 'update_ngo'),
    path('update_homepage/', views.update_homepage, name = 'update_homepage'),
    path('update_partners/', views.update_partners, name = 'update_partners'),
    path('update_resources/', views.update_resources, name = 'update_resources'),
    path('update_contactus/', views.update_contactus, name = 'update_contactus'),
    path('update_blog/<str:pk>/', views.update_blog, name = 'update_blog'),
    path('new_blog/<str:pk>/', views.new_blog, name = 'new_blog'),
    path('blog/<str:pk>', views.blog, name = 'blog'),
    path('all_blogs/<str:pk>', views.all_blogs, name = 'all_blogs'),
    
    path('reviews/<str:pk>/', views.reviews, name = 'reviews'),
    path('delete_ngo/<str:pk>/', views.delete_ngo, name = 'delete_ngo'),
    path('delete_blog/<str:pk>/', views.delete_blog, name = 'delete_blog'),
    path('user_profile/', views.user_profile, name = 'user_profile'),
    path('create_form/<str:pk>/', views.create_page, name = 'create_form'),
    path('edit_form/<str:pk>/', views.edit_page, name = 'edit_form'),
    path('update_donation/<str:pk>/', views.update_donation, name = 'update_donation'),
    
    path('verified/', views.verified, name = 'verified'),
    path('pending/', views.pending, name = 'pending'),

    path('charge/', views.charge, name = 'charge'),
    path('donations/', views.donations, name = 'donations'),
    path('success_msg/<str:args>/', views.success_msg, name = 'success_msg'),
    path('donation_instruction/<str:pk>/ ', views.donation_instruction, name = 'donation_instruction'),

    


]

#<str:pk>/