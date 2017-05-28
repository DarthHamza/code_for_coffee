
from django.shortcuts import render, redirect
import requests
from django.contrib.auth.models import User
from .forms import *

def home(request):
	url = "https://api.github.com/user/orgs"
	user = request.user
	social_account = user.socialaccount_set.get(user=user.id)
	token = social_account.socialtoken_set.get(account=social_account.id).token
	response = requests.get(url, headers={"Authorization":"token "+token})
	organization_list = response.json()

	return render(request, 'home.html', {"user": user, "object_list": organization_list})


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
