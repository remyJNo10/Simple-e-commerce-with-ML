from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Product
from login.models import History
from sklearn.metrics import jaccard_similarity_score as jss
# Create your views here.

@login_required(login_url='/')
def ShowHomepage(request):
	top_products = Product.objects.all()
	return render(request, "homepage/index.html",{'products' : top_products})

@login_required(login_url="/")
def ShowProduct(request,name):
	product = get_object_or_404(Product,name = name)
	all_products = Product.objects.all()
	all_product_tags = [([x.strip().lower() for x in item.product_tags.split(',')],item.name) for item in all_products]
	# print(all_product_tags)
	current_product_tags = [item.strip().lower() for item in product.product_tags.split(",")]
	jacardian_scores = [(jss(current_product_tags,x[0]),x[1]) for x in all_product_tags]
	jacardian_scores = sorted(jacardian_scores, reverse=True, key=lambda x: x[0])
	# print(jacardian_scores)
	recommendation = jacardian_scores[1][1]
	print(recommendation)
	recommendation = get_object_or_404(Product, name=recommendation)
	return render(request, "homepage/product.html",{'product' : product, "recommendation" : recommendation})

@login_required(login_url='/')
def buy(request,name):
	#if request.method == 'POST':
		user = request.user
		product = get_object_or_404(Product,name=name)
		history = History.objects.create(User=user,Product=product,date = timezone.now())
		history.save()
		return redirect('homepage:ShowHomepage')
		return render(request, "homepage/index.html")