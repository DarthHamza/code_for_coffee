
from django.shortcuts import render, redirect
import requests
import datetime
from django.contrib.auth.models import User
from .forms import *

def home(request):
	url = "https://api.github.com/user/orgs"
	user = request.user
	if request.user.is_authenticated():
		return redirect('dashboard')
	# social_account = user.socialaccount_set.get(user=user.id)
	# token = social_account.socialtoken_set.get(account=social_account.id).token
	# response = requests.get(url, headers={"Authorization":"token "+token})
	# organization_list = response.json()
	return render(request, 'home.html', {"user": user})

def dashboard(request):
	context={}
	usr = request.user
	today = datetime.date.today()
	coffee_list = Coffee.objects.filter(user=usr)
	order_list = Order.objects.filter(user=usr, date=today)
	context['usr']=usr
	context['date']=today
	context['coffee_list']=coffee_list
	context['order_list']=order_list
	return render(request, 'dashboard.html', context)

def createCoffee(request):
	context = {}
	if request.method == "POST":
		form = CoffeeForm(request.POST)
		context['form'] = form
		if form.is_valid():
			form.save()
			return redirect('/')
		else:
			return render(request, 'createCoffee.html', context)
	else:
		form = CoffeeForm()
		context['form'] = form
		return render(request, 'createCoffee.html', context)

def editCoffee(request, coffee_id):
	context = {}
	context['id'] = coffee_id
	coffee = Coffee.objects.get(id=coffee_id)
	if request.method == "POST":
		form = CoffeeForm(request.POST, instance=coffee)
		context['form'] = form
		if form.is_valid():
			form.save()
			return redirect('/')
		else:
			return render(request, 'editCoffee.html', context)
	else:
		form = CoffeeForm(instance=coffee)
		context['form'] = form
		return render(request, 'editCoffee.html', context)

def addOrder(request, coffee_id):
	context = {}
	context['id'] = coffee_id
	coffee = Coffee.objects.get(id=coffee_id)
	if request.method == "POST":
		form = OrderForm(request.POST)
		context['form'] = form
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = request.user
			obj.coffee = coffee
			obj.save()
			return redirect('/')
		else:
			return render(request, 'addOrder.html', context)
	else:
		form = OrderForm()
		context['form'] = form
		return render(request, 'addOrder.html', context)
