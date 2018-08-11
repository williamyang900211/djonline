from django.db import models

# Create your models here.
class Agency(models.Model):#组织信息表
	agency_name = models.CharField(max_length=128)

class Quoted_Price_Sheet_t(models.Model):#报价单
	sheet_number = models.CharField(unique=True,max_length=64)
	route_name = models.CharField(max_length=128)
	quoted_remarks = models.CharField(max_length=128,null=True)
	detail_quoted_price = models.TextField(max_length=5000)


class Quoted_Price_t(models.Model):#报价信息
	Quoted_Price_Sheet_t = models.ForeignKey(Quoted_Price_Sheet_t, on_delete=models.CASCADE)
	level = models.IntegerField()
	name = models.CharField(max_length= 32)
	quoted_price = models.FloatField()
	remarks = models.CharField(max_length=128,null=True)


class Request_sheet_t(models.Model):#出团申请单

	local_travel_agency_fk = models.ForeignKey(Agency, on_delete=models.CASCADE,related_name='local')
	travel_agency_name_fk = models.ForeignKey(Agency, on_delete=models.CASCADE)
	sheet_number = models.CharField(max_length=128)
	route_fk = models.ForeignKey(Quoted_Price_Sheet_t, on_delete=models.CASCADE)
	route_default_price = models.FloatField()
	startoff_date=models.DateField()


class TouristInfo_t(models.Model):#游客信息

	tname = models.CharField(max_length=50)
	tnum = models.IntegerField(default=1)
	quoted_price = models.FloatField()
	fixed_price = models.FloatField(default=0)
	ulti_price = models.FloatField()
	fixed_remarks = models.TextField(max_length=600,null=True)
	transfer_price = models.FloatField(default=0)
	transfer_to_fk = models.ForeignKey(Agency, on_delete=models.CASCADE,null=True)
	transfer_remarks = models.TextField(max_length=600,null=True)
	agency_price = models.FloatField(default=0)
	agency_remarks = models.TextField(max_length=600,null=True)
	request_sheet_fk = models.ForeignKey(Request_sheet_t, on_delete=models.CASCADE)

class Acct_Info_t(models.Model):#结算信息

	request_sheet_fk = models.ForeignKey(Request_sheet_t, on_delete=models.CASCADE)
	recieve_agency = models.ForeignKey(Agency, on_delete=models.CASCADE,related_name='recieve')
	paying_agency = models.ForeignKey(Agency, on_delete=models.CASCADE,related_name='paying')
	settlement_amount = models.FloatField()
	business_type = models.CharField(max_length=64)






