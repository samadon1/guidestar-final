from django.contrib import admin

# Register your models here.

from .models import Blog, ClaimProfile, ContactUs, Csv, DonationUse,Homepage, Ngo , Category , Message, NonProfits ,Page, DonationInstruction, Partners, Programs, Impact, Support, Reviews

admin.site.register(Ngo)
admin.site.register(Category)
admin.site.register(Message)
admin.site.register(Page)
admin.site.register(Programs)
admin.site.register(Impact)
admin.site.register(Support)
admin.site.register(DonationUse)
admin.site.register(DonationInstruction)
admin.site.register(Homepage)
admin.site.register(ContactUs)
admin.site.register(NonProfits)
admin.site.register(Partners)
admin.site.register(Blog)
admin.site.register(Reviews)
admin.site.register(Csv)
admin.site.register(ClaimProfile)


