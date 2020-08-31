from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from listings.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices
# Create your views here.
def index(request):     
    
    listings = Listing.objects.order_by('-list_date').filter(ispublished = True)[:3]
    context = {
        'price_choices' : price_choices,
        'bedroom_choices' : bedroom_choices,
        'state_choices' : state_choices,
        'listings' :listings,
    }
    return render(request, 'page/index.html',context)
    
def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtor = Realtor.objects.all().filter(is_mvp = True)
    context = {
        'realtors' : realtors ,
        'mvp_realtor' :mvp_realtor
    }
    return render(request, 'page/about.html',context)
    
    
