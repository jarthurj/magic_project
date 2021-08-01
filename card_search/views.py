from django.shortcuts import render, HttpResponse, redirect
from .models import *
def index(request):
	return render(request, "index.html")


# def clean_basic_search(input_str):
# 	string_list = input_str.lower().split()
# 	for s in string_list:
# 		s = s.capitalize()
# 	return " ".join(string_list)

def name_search(request):
	request.session['card_name'] = request.GET['name_search_input']
	return redirect("/name_search_return")

def name_search_return(request):
	card = Card.objects.filter(name=request.session['card_name']).first()
	context = {
		"name" : card.name,
		"url" : card.normal
	}
	return render(request, "single_card.html", context)

def advanced_search(request):
	return render(request, "advanced.html")

def advanced_search_process(request):
	colors = ""
	try:
		blue = request.GET['blue']
		colors += blue
	except:pass
	try:
		black = request.GET['black']
		colors += black
	except:pass
	try:
		green = request.GET['green']
		colors += green
	except:pass
	try:
		white = request.GET['white']
		colors += white
	except:pass
	try:
		red = request.GET['red']
		colors += red
	except:pass
	request.session['colors'] = Colors.objects.filter(color=colors.split())


	return redirect("/advanced_search_return")

def advanced_search_return(request):
	context = {
		'colors':request.session['colors']
	}
	request.session.flush()
	return render(request, "multi_card.html", context)
