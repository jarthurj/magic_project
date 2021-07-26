import pickle
from card_search.models import *
fh = open("..//all_artists2.p","rb")
artists = pickle.load(fh)
fh.close()

artists = list(artists)
for artist in artists:
	Artist.objects.create(artist_name = artist)

Digital.objects.create(digital=True)#id1
Digital.objects.create(digital=False)#id2

for x in range(1,7):
	Rarity.objects.create(rarity=x)

fh = open("..//set_names.p","rb")
set_names = pickle.load(fh)
fh.close()

for setx in set_names:
	Set_name.objects.create(set_name=setx)

fh = open("..//all_cards7-24.p","rb")
data = pickle.load(fh)
fh.close()

rare_dict = {'common':1,'uncommon':2,'rare':3,'mythic':4,'special':5,'bonus':6}

for x in range(1,21):
	if x not in [14,17,18,19]:
		Power.objects.create(power=x)
Power.objects.create(power=-1)
Power.objects.create(power=0)
Power.objects.create(power=99)

for x in range(1,21):
	if x not in [18,19]:
		Toughness.objects.create(toughness=x)
Toughness.objects.create(toughness=-1)
Toughness.objects.create(toughness=0)
Toughness.objects.create(toughness=99)

Colors.objects.create(color="W")#WHITE id=1
Colors.objects.create(color="B")#BLACK id=2
Colors.objects.create(color="G")#GREEN id=3
Colors.objects.create(color="U")#BLUE id=4
Colors.objects.create(color="R")#RED id=5
Colors.objects.create(color="C")#COLORLESS id=6

Color_identity.objects.create(color_iden="W")#WHITE id=1
Color_identity.objects.create(color_iden="B")#BLACK id=2
Color_identity.objects.create(color_iden="G")#GREEN id=3
Color_identity.objects.create(color_iden="U")#BLUE id=4
Color_identity.objects.create(color_iden="R")#RED id=5
Color_identity.objects.create(color_iden="C")#COLORLESS id=6

counter = 1
for card in data:
	Card.objects.create(
		name=card['name'],
		artist = Artist.objects.filter(artist_name=card['artist'])[0],
		digital = Digital.objects.filter(digital=card['digital'])[0],
		rarity = Rarity.objects.get(id=rare_dict[card['rarity']]),
	)
	counter += 1
	# try:
	# 	flavor_text = card['flavor_text']
	# 	card_to_update = Card.objects.get(id=count)
	# 	card_to_update.flavor_text = flavor_text
	# 	card_to_update.save()
	# except:
	# 	pass
	# try:
	# 	oracle_text = card['oracle_text']
	# 	card_to_update = Card.objects.get(id=count)
	# 	card_to_update.oracle_text = oracle_text
	# 	card_to_update.save()
	# except:
	# 	pass
	# try:
	# 	img_uris = card['image_uris']
	# 	card_to_update = Card.objects.get(id=count)
	# 	card_to_update.small = card['image_uris']['small']
	# 	card_to_update.normal = card['image_uris']['normal']
	# 	card_to_update.large = card['image_uris']['large']
	# 	card_to_update.save()
	# except:
	# 	pass
	# try:
	# 	power = card['power']
	# 	card_to_update=Card.objects.get(id=count)
	# 	if power in ['-1']:
	# 		card_to_update.power=Power.objects.get(id=17)
	# 	if power in ['+0','0']:
	# 		card_to_update.power=Power.objects.get(id=18)
	# 	if power in ['.5','1','+1', '1+*','1.5']:
	# 		card_to_update.power=Power.objects.get(id=1)
	# 	if power in ['2','+2','2+*', '2.5',]:
	# 		card_to_update.power=Power.objects.get(id=2)
	# 	if power in ['3','+3','3.5']:
	# 		card_to_update.power=Power.objects.get(id=3)
	# 	if power in ['4','+4']:
	# 		card_to_update.power=Power.objects.get(id=4)
	# 	if power in ['5']:
	# 		card_to_update.power=Power.objects.get(id=5)
	# 	if power in ['6']:
	# 		card_to_update.power=Power.objects.get(id=6)
	# 	if power in ['7']:
	# 		card_to_update.power=Power.objects.get(id=7)
	# 	if power in ['8']:
	# 		card_to_update.power=Power.objects.get(id=8)
	# 	if power in ['9']:
	# 		card_to_update.power=Power.objects.get(id=9)
	# 	if power in ['10']:
	# 		card_to_update.power=Power.objects.get(id=10)
	# 	if power in ['11']:
	# 		card_to_update.power=Power.objects.get(id=11)
	# 	if power in ['12']:
	# 		card_to_update.power=Power.objects.get(id=12)
	# 	if power in ['13']:
	# 		card_to_update.power=Power.objects.get(id=13)
	# 	if power in ['15']:
	# 		card_to_update.power=Power.objects.get(id=14)
	# 	if power in ['16']:
	# 		card_to_update.power=Power.objects.get(id=15)
	# 	if power in ['20']:
	# 		card_to_update.power=Power.objects.get(id=16)
	# 	if power in ['99']:
	# 		card_to_update.power=Power.objects.get(id=19)
	# 	card_to_update.save()
	# except:pass
	# try:
	# 	touhgness = card['toughness']
	# 	card_to_update=Card.objects.get(id=count)
	# 	if toughness in ['-1']:
	# 		card_to_update.toughness = Toughness.objects.get(id=19)
	# 	if toughness in ['0','-0','+0']:
	# 		card_to_update.toughness = Toughness.objects.get(id=20)
	# 	if toughness in ['.5','1','*+1','1+*','+1','1.5']:
	# 		card_to_update.toughness = Toughness.objects.get(id=1)
	# 	if toughness in ['2','+2','2.5','2+*']:
	# 		card_to_update.toughness = Toughness.objects.get(id=2)
	# 	if toughness in ['3','+3','3.5']:
	# 		card_to_update.toughness = Toughness.objects.get(id=3)
	# 	if toughness in ['4','+4']:
	# 		card_to_update.toughness = Toughness.objects.get(id=4)
	# 	if toughness in ['5']:
	# 		card_to_update.toughness = Toughness.objects.get(id=5)
	# 	if toughness in ['6']:
	# 		card_to_update.toughness = Toughness.objects.get(id=6)
	# 	if toughness in ['7','7-*']:
	# 		card_to_update.toughness = Toughness.objects.get(id=7)
	# 	if toughness in ['8']:
	# 		card_to_update.toughness = Toughness.objects.get(id=8)
	# 	if toughness in ['9']:
	# 		card_to_update.toughness = Toughness.objects.get(id=9)
	# 	if toughness in ['10']:
	# 		card_to_update.toughness = Toughness.objects.get(id=10)
	# 	if toughness in ['11']:
	# 		card_to_update.toughness = Toughness.objects.get(id=11)
	# 	if toughness in ['12']:
	# 		card_to_update.toughness = Toughness.objects.get(id=12)
	# 	if toughness in ['13']:
	# 		card_to_update.toughness = Toughness.objects.get(id=13)
	# 	if toughness in ['14']:
	# 		card_to_update.toughness = Toughness.objects.get(id=14)
	# 	if toughness in ['15']:
	# 		card_to_update.toughness = Toughness.objects.get(id=15)
	# 	if toughness in ['16']:
	# 		card_to_update.toughness = Toughness.objects.get(id=16)
	# 	if toughness in ['17']:
	# 		card_to_update.toughness = Toughness.objects.get(id=17)
	# 	if toughness in ['20']:
	# 		card_to_update.toughness = Toughness.objects.get(id=18)
	# 	if toughness in ['99']:
	# 		card_to_update.toughness = Toughness.objects.get(id=21)
	# 	card_to_update.save()
	# except:pass
	# try:
	# 	colors = card['colors']
	# 	this_card = Card.objects.get(id=counter)
	# 	for color in colors:
	# 		if color == "W":
	# 			this_color = Color.objects.get(id=1)
	# 			this_color.cards.add(this_card)
	# 		elif color == "B":
	# 			this_color = Color.objects.get(id=2)
	# 			this_color.cards.add(this_card)
	# 		elif color == "G":
	# 			this_color = Color.objects.get(id=3)
	# 			this_color.cards.add(this_card)
	# 		elif color == "U":
	# 			this_color = Color.objects.get(id=4)
	# 			this_color.cards.add(this_card)
	# 		elif color == "R":
	# 			this_color = Color.objects.get(id=5)
	# 			this_color.cards.add(this_card)
	# 		else:
	# 			this_color = Color.objects.get(id=6)
	# 			this_color.cards.add(this_card)
	# except: pass
	try:
		colors = card['color_identity']
		this_card = Card.objects.get(id=counter)
		for color in colors:
			if color == "W":
				this_color = Color_identity.objects.get(id=1)
				this_color.cards.add(this_card)
			elif color == "B":
				this_color = Color_identity.objects.get(id=2)
				this_color.cards.add(this_card)
			elif color == "G":
				this_color = Color_identity.objects.get(id=3)
				this_color.cards.add(this_card)
			elif color == "U":
				this_color = Color_identity.objects.get(id=4)
				this_color.cards.add(this_card)
			elif color == "R":
				this_color = Color_identity.objects.get(id=5)
				this_color.cards.add(this_card)
			else:
				this_color = Color_identity.objects.get(id=6)
				this_color.cards.add(this_card)
	except: pass
