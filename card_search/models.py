from django.db import models

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
	rare_list = ['common','uncommon','rare','mythic','special','bonus']

class Set_name(models.Model):
	set_name = models.CharField(max_length=50)

class Card(models.Model):
	name = models.CharField(max_length=150)
	flavor_text = models.CharField(max_length=450, null=True)
	oracle_text = models.CharField(max_length=1000, null=True)
	small = models.URLField()
	normal = models.URLField()
	large = models.URLField()

	artist = models.ForeignKey(Artist, related_name="cards", on_delete=models.CASCADE)
	digital = models.ForeignKey(Digital, related_name="cards", on_delete=models.CASCADE)
	rarity = models.ForeignKey(Rarity, related_name="cards", on_delete=models.CASCADE)
	set_name =models.ForeignKey(Set_name, related_name="cards", on_delete=models.CASCADE, null=True)

	power = models.ForeignKey(Power, related_name="cards", on_delete=models.CASCADE, null=True)
	toughness = models.ForeignKey(Toughness,related_name="cards", on_delete=models.CASCADE, null=True)

	# legalities
	# games
	# 	mtgo
	# 	paper
	# 	arena	


	# mana_cost
	# cmc
	# type_line
	# layout

	# keywords
class Colors(models.Model):
	color = models.CharField(max_length=1)
	cards = models.ManyToManyField(Card, related_name="colors")
class Color_identity(models.Model):
	color_iden = models.CharField(max_length=1)
	cards = models.ManyToManyField(Card, related_name="color_idens")
#Powers to clean up
# '∞','?', '*²', '*', 

#Toughness to clean up
# '?', '*²','*'
