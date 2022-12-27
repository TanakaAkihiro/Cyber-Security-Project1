from django.http import HttpResponse
#from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
from .models import Account, User
from django.db.models import Q
import json


#@login_required
def addView(request):
	user = request.user
	iban = request.POST.get("iban", "").strip()
	new = Account.objects.create(owner = user, iban = iban)
	return redirect('/')

#@login_required
def homePageView(request):
	try:
		if request.session['user'] is None:
			return redirect('/simplebank/login')
	except KeyError:
		return redirect('/simplebank/login')

	accounts = Account.objects.filter(owner=request.session.get('user'))
	return render(request, 'simplebank/index.html', dict(accounts=accounts))

def loginView(request):
	return render(request, 'simplebank/login.html')

def logoutView(request):
	request.session['user'] = None
	return redirect('/simplebank/login')

def loginActionView(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = User.objects.filter(username=username, password=password).first()
	
	if user is None:
		return redirect('/simplebank/login')

	request.session['user'] = str(user.id)
	if user:
		return redirect('/simplebank')
