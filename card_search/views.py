from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *
from django.core import serializers
import json
def index(request):
	return render(request, "index.html")


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
	form = AdvancedSearch()
	return render(request, "advanced.html", {"form":form})

def advanced_search_process(request):
	form = AdvancedSearch(request.POST)
	if form.is_valid():
		toughness_cards = Toughness.objects.toughness_query(request)
		color_cards = Colors.objects.colors_query(request)
		cards_list = []
		cards_to_return = color_cards.intersection(toughness_cards)
		data = serializers.serialize('json',cards_to_return[:60],fields=('name','normal','colors'))
		json_data = json.loads(data)
		request.session['returned_cards'] = json_data
	return redirect("/advanced_search_return")

def advanced_search_return(request):
	context = {
		'returned_cards':request.session['returned_cards'],
	}
	request.session.flush()
	return render(request, "multi_card.html", context)
