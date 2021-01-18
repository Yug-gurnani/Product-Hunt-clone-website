from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
def home(request):
	product = Product.objects
	return render(request,'home.html',{'products' : product})

@login_required(login_url = '/detail/signup')
def create(request):
	if request.method == 'POST':
		if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['image'] and request.FILES['icon']:
			product = Product()
			product.title = request.POST['title']
			product.body = request.POST['body']
			if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
				product.url = request.POST['url']
			else:
				product.url = "http://" + request.POST['url']
			product.image = request.FILES['image']
			product.icon = request.FILES['icon']
			product.date = timezone.datetime.now()
			product.hunter = request.user
			product.save()
			return redirect("/product/" + str(product.id))
		else:
			return render(request,'create.html',{'error': "All Fields are Required"})
	else:
		return render(request,'create.html')
def detail(request,product_id):
	product = get_object_or_404(Product,pk=product_id)
	return render(request,'detail.html',{'product':product})
@login_required(login_url = '/detail/signup')
def upvote(request,product_id):
	if request.method == 'POST':
		product = get_object_or_404(Product,pk=product_id)
		product.votes += 1
		product.save()
		return redirect("/product/" + str(product.id))