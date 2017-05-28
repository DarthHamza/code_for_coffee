from django.shortcuts import render
import requests
from django.contrib.auth.models import User
# Create your views here.
def home(request):
	url = "https://api.github.com/user/orgs"
	user = request.user
	social_account = user.socialaccount_set.get(user=user.id)
	token = social_account.socialtoken_set.get(account=social_account.id).token
	response = requests.get(url, headers={"Authorization":"token "+token})
	organization_list = response.json()
	# users = User.objects.all()
	return render(request, 'home.html', {"user": user, "object_list": organization_list})