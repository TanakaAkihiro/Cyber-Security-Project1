from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
#from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
from django.db import connection
#from django.core.signing import loads

from .models import Account, User
from django.db.models import Q
import json


#@login_required
@csrf_exempt
def addView(request):
	user = User.objects.get(pk=request.session['user'])
	iban = request.POST.get("iban", "").strip()
	new = Account.objects.create(owner = user, iban = iban)
	return redirect('/')

#@login_required
@csrf_exempt
def homePageView(request):
	try:
		if request.session['user'] is None:
			return redirect('/simplebank/login')
	except KeyError:
		return redirect('/simplebank/login')
	user_id = request.session['user']

	query = 'SELECT iban FROM simplebank_account a JOIN simplebank_user u ON a.owner_id = u.id WHERE u.id = ' + user_id
	with connection.cursor() as cursor:
		cursor.execute(query)
		rows = cursor.fetchall()

	accounts = []
	for r in rows:
		accounts.append(r[0])

	# Fix for flaw 2: instead of lines 31 - 38, use the code below
	# accounts = Account.objects.filter(owner=request.session.get('user'))
	
	return render(request, 'simplebank/index.html', dict(accounts=accounts))

@csrf_exempt
def loginView(request):
	return render(request, 'simplebank/login.html')

@csrf_exempt
def logoutView(request):
	request.session['user'] = None
	return redirect('/simplebank/login')

@csrf_exempt
def loginActionView(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = User.objects.filter(username=username, password=password).first()
	#user = User.objects.filter(username=username, password=loads(password)).first()
	
	if user is None:
		return redirect('/simplebank/login')

	request.session['user'] = str(user.id)
	if user:
		return redirect('/simplebank')
