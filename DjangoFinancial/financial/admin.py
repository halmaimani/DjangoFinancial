from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
# Register your models here.

from .models import  Customer, Stock, Cryptocurrency

admin.site.register(Customer)
admin.site.register(Stock)
admin.site.register(Cryptocurrency)


admin.site.site_header = "Django Financial"
admin.site.site_title = "Django Financial"
