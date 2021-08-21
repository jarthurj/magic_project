from django.db import models
rare_list = ['common','uncommon','rare','mythic','special','bonus']

class ToughnessManager(models.Manager):
	def toughness_query(self, request):
		toughness = request.POST['toughness']
		toughness_equality = request.POST['toughness_equality']
		if toughness == '99':
			return None
		elif toughness_equality == '1':#equals
			return Toughness.objects.filter(toughness=int(toughness)).first().cards.all()
		elif toughness_equality == '2':#gte
			return Toughness.objects.filter(toughness__gte=int(toughness)).first().cards.all()
		elif toughness_equality == '3':#lte
			return Toughness.objects.filter(toughness__lte=int(toughness)).first().cards.all()
		elif toughness_equality == '4':#gt
			return Toughness.objects.filter(toughness__gt=int(toughness)).first().cards.all()
		elif toughness_equality == '5':#lt
			return Toughness.objects.filter(toughness__lt=int(toughness)).first().cards.all()


class Toughness(models.Model):
	toughness = models.IntegerField()
	objects = ToughnessManager()
class PowerManager(models.Manager):
	def power_query(self, request):
		power = request.POST['power']
		power_equality = request.POST['power_equality']
		if power == '99':
			return None
		elif power_equality == '1':#equals
			return Power.objects.filter(power=int(power)).first().cards.all()
		elif power_equality == '2':#gte
			return Power.objects.filter(power__gte=int(power)).first().cards.all()
		elif power_equality == '3':#lte
			return Power.objects.filter(power__lte=int(power)).first().cards.all()
		elif power_equality == '4':#gt
			return Power.objects.filter(power__gt=int(power)).first().cards.all()
		elif power_equality == '5':#lt
			return Power.objects.filter(power__lt=int(power)).first().cards.all()


class Power(models.Model):
	power = models.IntegerField()
	objects = PowerManager()

class ArtistManager(models.Manager):
	def artist_query(self, request):
		artist_name = request.POST['artist']
		if artist_name == "":
			return None
		
		artists = Artist.objects.filter(artist_name__icontains=artist_name)
		artist_cards = Card.objects.none()
		for a in artists:
			if len(a.cards.all()) > 0:
				artist_cards = artist_cards.union(a.cards.all())
		return artist_cards
class Artist(models.Model):
	artist_name = models.CharField(max_length=55)
	objects = ArtistManager()
class Digital(models.Model):
	digital = models.BooleanField()

class RarityManager(models.Manager):
	def rarity_query(self, request):
		if request.POST['rarity'] == '0':
			return None
		else:
			return Rarity.objects.filter(rarity=int(request.POST['rarity'])).first().cards.all()
class Rarity(models.Model):
	rarity = models.IntegerField()
	objects = RarityManager()

class SetManager(models.Manager):
	def set_query(self, request):
		if request.POST['s_name'] == "0":
			return None
		else:
			sets = Set_name.objects.all().order_by('set_name')
			cards = sets[int(request.POST['s_name']) - 1].cards.all()
			return cards
class Set_name(models.Model):
	set_name = models.CharField(max_length=50)
	objects = SetManager()
class Layout(models.Model):
	layout= models.CharField(max_length=45)

class ManaManager(models.Manager):
	def mana_query(request):
		pass
class Mana_cost(models.Model):
	mana_cost= models.CharField(max_length=45)
	objects = ManaManager()


class CmcManager(models.Manager):
	def cmc_query(self, request):
		cmc = request.POST['cmc_q']
		cmc_equality = request.POST['cmc_equality']
		if cmc == '99':
			return None
		elif cmc_equality == '1':#equals
			return Cmc.objects.filter(cmc=int(cmc)).first().cards.all()
		elif cmc_equality == '2':#gte
			return Cmc.objects.filter(cmc__gte=int(cmc)).first().cards.all()
		elif cmc_equality == '3':#lte
			return Cmc.objects.filter(cmc__lte=int(cmc)).first().cards.all()
		elif cmc_equality == '4':#gt
			return Cmc.objects.filter(cmc__gt=int(cmc)).first().cards.all()
		elif cmc_equality == '5':#lt
			return Cmc.objects.filter(cmc__lt=int(cmc)).first().cards.all()
class Cmc(models.Model):
	cmc = models.FloatField()
	objects = CmcManager()
class Legalities(models.Model):
	name = models.CharField(max_length=45)

class Card(models.Model):
	name = models.CharField(max_length=150)
	flavor_text = models.CharField(max_length=450, null=True)
	oracle_text = models.CharField(max_length=1000, null=True)

	small = models.URLField()
	normal = models.URLField()
	large = models.URLField()

	type_line = models.CharField(max_length=100, null=True)

	artist = models.ForeignKey(Artist, related_name="cards", on_delete=models.CASCADE)
	digital = models.ForeignKey(Digital, related_name="cards", on_delete=models.CASCADE)
	rarity = models.ForeignKey(Rarity, related_name="cards", on_delete=models.CASCADE)
	set_name =models.ForeignKey(Set_name, related_name="cards", on_delete=models.CASCADE, null=True)

	power = models.ForeignKey(Power, related_name="cards", on_delete=models.CASCADE, null=True)
	toughness = models.ForeignKey(Toughness,related_name="cards", on_delete=models.CASCADE, null=True)

	layout = models.ForeignKey(Layout, related_name="cards", on_delete=models.CASCADE, null=True)
	mana_cost = models.ForeignKey(Mana_cost, related_name="cards", on_delete=models.CASCADE,null=True)
	cmc = models.ForeignKey(Cmc, related_name="cards", on_delete=models.CASCADE,null=True)

class Legal(models.Model):
	name = models.ForeignKey(Legalities, related_name="legals", on_delete=models.CASCADE)
	legal = models.BooleanField(null=True)
	card = models.ForeignKey(Card, related_name="legals", on_delete=models.CASCADE, null=True)


class Colors_Manager(models.Manager):
	def colors_query(self,request):
		xors = request.POST["colors_options"]
		colors = request.POST.getlist("colors")
		if len(colors) == 0:
			return None
		not_colors = "RBWGU"
		for color in colors:
			not_colors = not_colors.replace(color, "")
		color_cards = Colors.objects.filter(color=colors[0]).first().cards.all()
		not_color_cards = Colors.objects.filter(color=not_colors[0]).first().cards.all()
		if xors[0] == '1':
			for x in range(1,len(colors)):
				color_cards = color_cards.union(Colors.objects.filter(color=colors[x]).first().cards.all())
			for x in range(1,len(not_colors)):
				not_color_cards = not_color_cards.union(Colors.objects.filter(color=not_colors[x]).first().cards.all())
			return color_cards.difference(color_cards.intersection(not_color_cards))
		else:
			for x in range(1,len(colors)):
				color_cards = color_cards.union(Colors.objects.filter(color=colors[x]).first().cards.all())
			return color_cards

class Colors(models.Model):
	color = models.CharField(max_length=1)
	cards = models.ManyToManyField(Card, related_name="colors")
	objects = Colors_Manager()

class Color_identity(models.Model):
	color_iden = models.CharField(max_length=1)
	cards = models.ManyToManyField(Card, related_name="color_idens")

class KeywordManager(models.Manager):
	def keyword_query(self, request):
		if request.POST['keyword'] == '0':
			return None
		else:
			keyword = request.POST['keyword']
			keyword_cards = Keyword.objects.get(id=int(keyword)).cards.all()
			return keyword_cards
class Keyword(models.Model):
	keyword = models.CharField(max_length=45)
	cards = models.ManyToManyField(Card, related_name="keywords")
	objects = KeywordManager()

class CardTypeManager(models.Manager):
	def card_type_query(self, request):
		if request.POST['card_type'] == '0':
			return None
		else:
			card_type = request.POST['card_type']
			cards = Card_type.objects.get(id=int(card_type)).cards.all()
			return cards
class Card_type(models.Model):
	card_type= models.CharField(max_length=45)
	cards = models.ManyToManyField(Card,related_name="card_types")
	objects = CardTypeManager()
#Powers to clean up
# '∞','?', '*²', '*', 

#Toughness to clean up
# '?', '*²','*'


