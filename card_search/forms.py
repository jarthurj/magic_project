from django import forms

COLORS = (
	('B','Black'),
	('W','White'),
	('R','Red'),
	('G','Green'),
	('U','Blue'),
)


XORS = (
	(1,'Only These Colors'),
	(2,'Includes These Colors'),
)

TOUGHNESS = (
	(99,'-'),
	(0,'0'),
	(1,'1'),
	(2,'2'),
	(3,'3'),
	(4,'4'),
	(5,'5'),
	(6,'6'),
	(7,'7'),
	(8,'8'),
	(9,'9'),
	(10,'10'),
	(11,'11'),
	(12,'12'),
	(13,'13'),
	(14,'14'),
	(15,'15'),
	(16,'16'),
	(17,'17'),
	(18,'18'),
	(19,'19'),
	(20,'20'),
)

TOUGHNESS_MOD = (
	(1,"="),
	(2,"\u2265"),
	(3,"\u2264"),
	(4,">"),
	(5,"<")
)
POWER = (
	(99,'-'),
	(0,'0'),
	(1,'1'),
	(2,'2'),
	(3,'3'),
	(4,'4'),
	(5,'5'),
	(6,'6'),
	(7,'7'),
	(8,'8'),
	(9,'9'),
	(10,'10'),
	(11,'11'),
	(12,'12'),
	(13,'13'),
	(14,'14'),
	(15,'15'),
	(16,'16'),
	(17,'17'),
	(18,'18'),
	(19,'19'),
	(20,'20'),
)

POWER_MOD = (
	(1,"="),
	(2,"\u2265"),
	(3,"\u2264"),
	(4,">"),
	(5,"<")
)

RARITY = (
	(0,"-"),
	(1,"Common"),
	(2,"Uncommon"),
	(3,"Rare"),
	(4,"Mythic"),
	(5,"Special"),
	(6,"Bonus")
)
class AdvancedSearch(forms.Form):

	colors = forms.MultipleChoiceField(
		choices=COLORS,
		label="Colors",
		required=False,
		widget=forms.CheckboxSelectMultiple,
		)
	colors_options = forms.ChoiceField(
		choices =XORS,
		label="Colors Modifier",
		required=False,
		widget=forms.Select(choices=XORS)
		)
	toughness_equality = forms.ChoiceField(
		choices =TOUGHNESS_MOD,
		label="Toughness",
		required=False,
		widget=forms.Select(choices=TOUGHNESS_MOD)
		)
	toughness = forms.ChoiceField(
		choices =TOUGHNESS,
		label="",
		required=False,
		widget=forms.Select(choices=TOUGHNESS)
		)

	power_equality = forms.ChoiceField(
		choices =POWER_MOD,
		label="Power",
		required=False,
		widget=forms.Select(choices=POWER_MOD)
		)
	power = forms.ChoiceField(
		choices =POWER,
		label="",
		required=False,
		widget=forms.Select(choices=POWER)
		)
	artist = forms.CharField(
		label="Artist",
		required=False,
		)

	rarity = forms.ChoiceField(
		choices =RARITY,
		label="Rarity",
		required=False,
		widget=forms.Select(choices=RARITY)
		)