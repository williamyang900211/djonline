from django.contrib import admin
from acct.models import Agency,Quoted_Price_Sheet_t,Quoted_Price_t,Request_sheet_t,TouristInfo_t,Acct_Info_t

# Register your models here.
admin.site.register(Agency)
admin.site.register(Quoted_Price_t)
admin.site.register(Quoted_Price_Sheet_t)
admin.site.register(Request_sheet_t)
admin.site.register(TouristInfo_t)
admin.site.register(Acct_Info_t)