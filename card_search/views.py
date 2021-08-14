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
		power_cards = Power.objects.power_query(request)
		artist_cards = Artist.objects.artist_query(request)
		rarity_cards = Rarity.objects.rarity_query(request)
		cards_list = [toughness_cards, power_cards, color_cards,
					artist_cards, rarity_cards]
		while None in cards_list:
			cards_list.remove(None)
		if len(cards_list) > 1:
			cards_to_return = cards_list[0].intersection(*cards_list[1:])
		elif len(cards_list) == 0:
			cards_to_return = Card.objects.all()
		else:
			cards_to_return = cards_list[0]
		data = serializers.serialize('json',cards_to_return[:60],fields=('name','small'))
		json_data = json.loads(data)
		request.session['returned_cards'] = json_data
	return redirect("/advanced_search_return")

def advanced_search_return(request):
	context = {
		'returned_cards':request.session['returned_cards'],
	}
	request.session.flush()
	return render(request, "multi_card.html", context)
