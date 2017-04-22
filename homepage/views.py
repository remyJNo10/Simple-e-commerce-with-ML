from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Product
from login.models import History
from sklearn.metrics import jaccard_similarity_score as jss
from random import randint
# Create your views here.

@login_required(login_url='/')
def ShowHomepage(request):
	user = request.user
	top_products = Product.objects.all()
	history = History.objects.filter(User=user)
	recommendations = set()
	if history.exists():
		history = history[0]
		for i in history.bought_items.split(",")[:-4]:
			product = get_object_or_404(Product,name = i)
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
			recommendations.add(recommendation)

	return render(request, "homepage/index.html",{'products' : top_products,'recommendations' : list(recommendations)})

@login_required(login_url='/')
def ShowProduct(request,name):
	product = get_object_or_404(Product,name = name)
	print(product)
	print("first")
	all_products = Product.objects.all()
	all_product_tags = [([x.strip().lower() for x in item.product_tags.split(',')],item.name) for item in all_products]
	# print(all_product_tags)
	current_product_tags = [item.strip().lower() for item in product.product_tags.split(",")]
	jacardian_scores = [(jss(current_product_tags,x[0]),x[1]) for x in all_product_tags]
	jacardian_scores = sorted(jacardian_scores, reverse=True, key=lambda x: x[0])
	# print(jacardian_scores)
	recommendations = [b[1] for b in jacardian_scores[1:5]]
	rec = []
	print(recommendations)
	for i in recommendations:
		rec.append(get_object_or_404(Product, name=i))
	print("loop")
	customers_also_bought = []
	e = History.objects.all()
	e = [x.bought_items for x in e]
	user = request.user
	curr = History.objects.filter(User=user)[0].bought_items
	e = [x for x in e if x!=curr]
	e = [x for x in e if product.name in x ]
	if len(e) != 0:
		g = randint(0,len(e)-1)
		print(g)
		print(e[g])
		customers_also_bought = [get_object_or_404(Product, name=d) for d in e[g]]
	print("render")
	return render(request, "homepage/product.html",{'product' : product, "recommendations" : rec, "also":customers_also_bought})

@login_required(login_url='/')
def buy(request,name):
	user = request.user
	product = Product.objects.filter(name=name)[0]
	if user.username not in str(product.buyer_list).split(","):
		product.buyer_list = str(product.buyer_list)+","+user.username
		product.save()
	history = History.objects.filter(User=user)
	if not history.exists():
		history = History.objects.create(User=user,bought_items=str(product))
		history.save()
	else:
		history = history[0]
		history.bought_items = history.bought_items + "," + str(product)
		history.save()
	return redirect('homepage:ShowHomepage')
	# return render(request, "homepage/index.html")