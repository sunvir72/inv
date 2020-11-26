from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from Link5.models import part
from django.contrib import messages
#import pandas as pd
#from django.core.files.base import ContentFile
import os
import datetime
from django.http import JsonResponse
import copy

def Link5(request):
    return render(request, 'Link5.html',{})

def viewInventory(request):
	if request.method=='POST':
		try:
			name1=request.POST['pname']
			stock1=request.POST['stock']
			mc1=request.POST['mc']
			sc1=request.POST['sc']
			a=part.objects.get(name=name1)
			a.stock=stock1
			a.manufacturing_cost=mc1
			a.selling_cost=sc1
			a.save()
		except:
			name1=request.POST['pname']
			stock1=request.POST['stock']
			mc1=request.POST['mc']
			sc1=request.POST['sc']
			a=part(name=name1,stock=stock1,manufacturing_cost=mc1,selling_cost=sc1)
			a.save()
	all_parts=part.objects.all()
	return render(request, 'viewInv.html', {'all_parts':all_parts})
            
def updateInventory(request):
    if request.method=='POST':
    	pid=request.POST['pid']
    	name1=request.POST['pname']
    	stock1=request.POST['stock']
    	mc1=request.POST['mc']
    	sc1=request.POST['sc']
    	a=part.objects.get(id=pid)
    	a.name=name1
    	a.stock=stock1
    	a.manufacturing_cost=mc1
    	a.selling_cost=sc1
    	a.save()
    all_parts=part.objects.all()
    return render(request, 'viewInv.html', {'all_parts':all_parts})

    
def deleteEntry(request,eid):
    a=part.objects.get(id=eid)
    a.delete()
    all_parts=part.objects.all()
    return render(request, 'viewInv.html', {'all_parts':all_parts})

def addSales(request):
	if request.method=='POST':
		pname=request.POST['pname']
		sold=request.POST['qs']
		a=part.objects.get(name=pname)
		#>0
		a.stock=a.stock-int(sold)
		a.save()
		messages.success(request,('Sale Added'))
	all_parts=part.objects.all()
	return render(request, 'addSales.html', {'all_parts':all_parts})