from django.db import models

rare_list = ['common','uncommon','rare','mythic','special','bonus']

class Toughness(models.Model):
	toughness = models.IntegerField()

class Power(models.Model):
	power = models.IntegerField()

class Artist(models.Model):
	artist_name = models.CharField(max_length=55)

class Digital(models.Model):
	digital = models.BooleanField()

class Rarity(models.Model):
	rarity = models.IntegerField()

class Set_name(models.Model):
	set_name = models.CharField(max_length=50)

class Layout(models.Model):
	layout= models.CharField(max_length=45)

class Mana_cost(models.Model):
	mana_cost= models.CharField(max_length=45)

class Cmc(models.Model):
	cmc = models.FloatField()

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

class Colors(models.Model):
	color = models.CharField(max_length=1)
	cards = models.ManyToManyField(Card, related_name="colors")
class Color_identity(models.Model):
	color_iden = models.CharField(max_length=1)
	cards = models.ManyToManyField(Card, related_name="color_idens")
class Keyword(models.Model):
	keyword = models.CharField(max_length=45)
	cards = models.ManyToManyField(Card, related_name="keywords")

class Card_type(models.Model):
	card_type= models.CharField(max_length=45)
	cards = models.ManyToManyField(Card,related_name="card_types")
#Powers to clean up
# '∞','?', '*²', '*', 

#Toughness to clean up
# '?', '*²','*'
