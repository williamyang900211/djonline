from django.shortcuts import render
from acct.models import Request_sheet_t,Agency,TouristInfo_t
import math
# Create your views here.
def index(request):

	return render(request, 'acct/index.html')

def calculate_acct(tourists):
	ultip_sum=0#最终报价之和
	agencyp_sum=0#代收金额之和
	daishou_amount = 0 #非调拨的代收金额之和
	diaobo_business ={}
	for t in tourists:
		ultip_sum = t.ulti_price+ultip_sum
		agencyp_sum= t.agency_price+ agencyp_sum
		diaobodanwei = t.transfer_to_fk.agency_name
		if diaobodanwei =='':
			daishou_amount = daishou_amount + t.agency_price
		else:
			if diaobodanwei in diaobo_business.keys():
				diaobo_business[diaobodanwei]= diaobo_business[diaobodanwei] + t.transfer_price- t.agency_price
			else:
				diaobo_business[diaobodanwei]=t.transfer_price- t.agency_price                  
	amount = ultip_sum - agencyp_sum
	result = {'amount':amount,'daishou_amount':daishou_amount,'diaobo_business':diaobo_business}	
	
	
	return result

def request_form(request):

	rs = Request_sheet_t.objects.all()[0]
	local_travel_agency_name = rs.local_travel_agency_fk.agency_name
	travel_agency_name = rs.travel_agency_name_fk.agency_name
	tourists = TouristInfo_t.objects.filter(request_sheet_fk__pk=rs.id)
    
	result =calculate_acct(tourists)
	skyw_amount=result['amount']
	daishou_amount=result['daishou_amount']
	diaobo_business = result['diaobo_business']
	if skyw_amount>0 or skyw_amount==0:
		shoukuang_fang = local_travel_agency_name
		fukuang_fang = travel_agency_name
	else:
		shoukuang_fang = travel_agency_name
		fukuang_fang = local_travel_agency_name
	
	jiesuan_info =[]
	jiesuan_info.append(
		{'shoukuang_fang':shoukuang_fang,'fukuang_fang':fukuang_fang,
		'amount':abs(skyw_amount),'yewuleixing':'散客业务'}
		)
	jiesuan_info.append(
		{'shoukuang_fang':local_travel_agency_name,	'fukuang_fang':'游客','amount':daishou_amount,'yewuleixing':'代收业务'}
		)
	keys = list(diaobo_business.keys())
	for key in keys:
		if diaobo_business[key]>0 or diaobo_business[key]==0:
			jiesuan_info.append(
			{
			'shoukuang_fang':key,
			'fukuang_fang':local_travel_agency_name,
			'amount':diaobo_business[key],
			'yewuleixing':'调拨业务'
			})
		else:
			jiesuan_info.append(
				{
				'shoukuang_fang':key,
			    'fukuang_fang':local_travel_agency_name,
			    'amount':diaobo_business[key],
			    'yewuleixing':'调拨业务'
				}
			)

		







	context_dict={'ltan':local_travel_agency_name,
	'tan':travel_agency_name,
	'sheet_number':rs.sheet_number,
	'rtfk':rs.route_fk.route_name,
	'rdp':rs.route_default_price,
	'date':rs.startoff_date,
	'tourists':tourists,
	'jiesuan_info':jiesuan_info,
	}
	return render(request, 'acct/request_form.html',context=context_dict)