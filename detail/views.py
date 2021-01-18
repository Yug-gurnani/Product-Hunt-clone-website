from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
def signup(request):
	if request.method == "POST":
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username = request.POST['username'])
				return render(request,'signup.html',{'error' : 'Username already Exist'})
			except User.DoesNotExist:
				user = User.objects.create_user(username=request.POST["username"],password=request.POST['password1'])
				auth.login(request,user)
				return redirect('home')
		else:
			return render(request,'signup.html',{'error' : 'Password Should Match'})
	else:
		return render(request,'signup.html')

def login(request):
	if request.method == "POST":
		user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
		if user:
			auth.login(request,user)
			return redirect('home')
		else:
			return render(request,'login.html',{'error' : 'Username or Password is Incorrect'})
	else:
		return render(request,'login.html')

def logout(request):
	if request.method == "POST":
		auth.logout(request)
		return redirect('home')
