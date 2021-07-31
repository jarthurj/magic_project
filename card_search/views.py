from django.shortcuts import render, HttpResponse, redirect
from card_search.models import *
def index(request):
	return render(request, "index.html")


# def clean_basic_search(input_str):
# 	string_list = input_str.lower().split()
# 	for s in string_list:
# 		s = s.capitalize()
# 	return " ".join(string_list)

def name_search(request):
	request.session['card_name'] = request.POST['name_search_input']
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
	try:
		request.session['colors'] =request.POST['blue']+request.POST['black']+request.POST['green']+request.POST['white']+request.POST['red']
		request.session['blue'] = request.POST['blue']
		request.session['black'] = request.POST['black']
		request.session['green'] = request.POST['green']
		request.session['white'] = request.POST['white']
		request.session['red'] = request.POST['red']

	except:pass
	return redirect("/advanced_search_return")

def advanced_search_return(request):
	context = {
		# 'blue':request.session['blue'],
		# 'black':request.session['black'],
		# 'green':request.session['green'],
		# 'white':request.session['white'],
		# 'red':request.session['red'],
		'colors':request.session['colors']
	}
	request.session.flush()
	return render(request, "multi_card.html", context)
