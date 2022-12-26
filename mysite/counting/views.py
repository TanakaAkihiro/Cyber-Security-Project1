from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Account
from django.db.models import Q
import json



def addView(request):
	user = request.user
	iban = request.POST.get("iban", "").strip()
	new = Account.objects.create(owner = user, iban = iban)
	return redirect('/')


def homePageView(request):
    return HttpResponse('moi')
	#user = request.user
	#accounts = Account.objects.filter(owner=user)
	#return render(request, 'pages/index.html', dict(accounts=accounts))
