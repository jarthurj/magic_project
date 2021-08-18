from django import forms
from django.forms import ModelForm
from .models import *
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

SETS = (
	( 0 , "-"),
	( 1 , "15th Anniversary Cards" ),
	( 2 , "2016 Heroes of the Realm" ),
	( 3 , "2017 Gift Pack" ),
	( 4 , "2017 Heroes of the Realm" ),
	( 5 , "2018 Heroes of the Realm" ),
	( 6 , "2018 Lunar New Year" ),
	( 7 , "2019 Heroes of the Realm" ),
	( 8 , "2021 Lunar New Year" ),
	( 9 , "Adventures in the Forgotten Realms" ),
	( 10 ,"Adventures in the Forgotten Realms Art Series" ),
	( 11 ,"Adventures in the Forgotten Realms Promos" ),
	( 12 ,"Adventures in the Forgotten Realms Tokens" ),
	( 13 ,"Aether Revolt" ),
	( 14 ,"Aether Revolt Promos" ),
	( 15 ,"Aether Revolt Tokens" ),
	( 16 ,"Alara Reborn" ),
	( 17 ,"Alara Reborn Promos" ),
	( 18 ,"Alara Reborn Tokens" ),
	( 19 ,"Alliances" ),
	( 20 ,"Amonkhet" ),
	( 21 ,"Amonkhet Invocations" ),
	( 22 ,"Amonkhet Promos" ),
	( 23 ,"Amonkhet Remastered" ),
	( 24 ,"Amonkhet Tokens" ),
	( 25 ,"Anthologies" ),
	( 26 ,"Antiquities" ),
	( 27 ,"Apocalypse" ),
	( 28 ,"Apocalypse Promos" ),
	( 29 ,"Arabian Nights" ),
	( 30 ,"Archenemy" ),
	( 31 ,"Archenemy Schemes" ),
	( 32 ,"Archenemy: Nicol Bolas" ),
	( 33 ,"Archenemy: Nicol Bolas Schemes" ),
	( 34 ,"Archenemy: Nicol Bolas Tokens" ),
	( 35 ,"Arena Beginner Set" ),
	( 36 ,"Arena League 1996" ),
	( 37 ,"Arena League 1999" ),
	( 38 ,"Arena League 2000" ),
	( 39 ,"Arena League 2001" ),
	( 40 ,"Arena League 2002" ),
	( 41 ,"Arena League 2003" ),
	( 42 ,"Arena League 2004" ),
	( 43 ,"Arena League 2005" ),
	( 44 ,"Arena League 2006" ),
	( 45 ,"Arena New Player Experience" ),
	( 46 ,"Arena New Player Experience Cards" ),
	( 47 ,"Arena New Player Experience Extras" ),
	( 48 ,"Asia Pacific Land Program" ),
	( 49 ,"Astral Cards" ),
	( 50 ,"Avacyn Restored" ),
	( 51 ,"Avacyn Restored Promos" ),
	( 52 ,"Avacyn Restored Tokens" ),
	( 53 ,"BFZ Standard Series" ),
	( 54 ,"Battle Royale Box Set" ),
	( 55 ,"Battle for Zendikar" ),
	( 56 ,"Battle for Zendikar Promos" ),
	( 57 ,"Battle for Zendikar Tokens" ),
	( 58 ,"Battle the Horde" ),
	( 59 ,"Battlebond" ),
	( 60 ,"Battlebond Promos" ),
	( 61 ,"Battlebond Tokens" ),
	( 62 ,"Beatdown Box Set" ),
	( 63 ,"Betrayers of Kamigawa" ),
	( 64 ,"Betrayers of Kamigawa Promos" ),
	( 65 ,"Born of the Gods" ),
	( 66 ,"Born of the Gods Hero's Path" ),
	( 67 ,"Born of the Gods Promos" ),
	( 68 ,"Born of the Gods Tokens" ),
	( 69 ,"Celebration Cards" ),
	( 70 ,"Champions of Kamigawa" ),
	( 71 ,"Champions of Kamigawa Promos" ),
	( 72 ,"Champs and States" ),
	( 73 ,"Chronicles" ),
	( 74 ,"Classic Sixth Edition" ),
	( 75 ,"Coldsnap" ),
	( 76 ,"Coldsnap Promos" ),
	( 77 ,"Coldsnap Theme Decks" ),
	( 78 ,"Collectors’ Edition" ),
	( 79 ,"Commander 2011" ),
	( 80 ,"Commander 2011 Launch Party" ),
	( 81 ,"Commander 2011 Oversized" ),
	( 82 ,"Commander 2013" ),
	( 83 ,"Commander 2013 Oversized" ),
	( 84 ,"Commander 2014" ),
	( 85 ,"Commander 2014 Oversized" ),
	( 86 ,"Commander 2014 Tokens" ),
	( 87 ,"Commander 2015" ),
	( 88 ,"Commander 2015 Oversized" ),
	( 89 ,"Commander 2015 Tokens" ),
	( 90 ,"Commander 2016" ),
	( 91 ,"Commander 2016 Oversized" ),
	( 92 ,"Commander 2016 Tokens" ),
	( 93 ,"Commander 2017" ),
	( 94 ,"Commander 2017 Oversized" ),
	( 95 ,"Commander 2017 Tokens" ),
	( 96 ,"Commander 2018" ),
	( 97 ,"Commander 2018 Oversized" ),
	( 98 ,"Commander 2018 Tokens" ),
	( 99 ,"Commander 2019" ),
	( 100 , "Commander 2019 Oversized" ),
	( 101 , "Commander 2019 Tokens" ),
	( 102 , "Commander 2020" ),
	( 103 , "Commander 2020 Oversized" ),
	( 104 , "Commander 2020 Tokens" ),
	( 105 , "Commander 2021" ),
	( 106 , "Commander 2021 Display Commanders" ),
	( 107 , "Commander 2021 Tokens" ),
	( 108 , "Commander Anthology" ),
	( 109 , "Commander Anthology Tokens" ),
	( 110 , "Commander Anthology Volume II" ),
	( 111 , "Commander Anthology Volume II Tokens" ),
	( 112 , "Commander Collection: Green" ),
	( 113 , "Commander Legends" ),
	( 114 , "Commander Legends Tokens" ),
	( 115 , "Commander's Arsenal" ),
	( 116 , "Commander's Arsenal Oversized" ),
	( 117 , "Conflux" ),
	( 118 , "Conflux Promos" ),
	( 119 , "Conflux Tokens" ),
	( 120 , "Conspiracy" ),
	( 121 , "Conspiracy Promos" ),
	( 122 , "Conspiracy Tokens" ),
	( 123 , "Conspiracy: Take the Crown" ),
	( 124 , "Conspiracy: Take the Crown Tokens" ),
	( 125 , "Core Set 2019" ),
	( 126 , "Core Set 2019 Promos" ),
	( 127 , "Core Set 2019 Tokens" ),
	( 128 , "Core Set 2020" ),
	( 129 , "Core Set 2020 Promos" ),
	( 130 , "Core Set 2020 Tokens" ),
	( 131 , "Core Set 2021" ),
	( 132 , "Core Set 2021 Promos" ),
	( 133 , "Core Set 2021 Tokens" ),
	( 134 , "DCI Legend Membership" ),
	( 135 , "Dark Ascension" ),
	( 136 , "Dark Ascension Promos" ),
	( 137 , "Dark Ascension Tokens" ),
	( 138 , "Darksteel" ),
	( 139 , "Darksteel Promos" ),
	( 140 , "Deckmasters" ),
	( 141 , "Defeat a God" ),
	( 142 , "Dissension" ),
	( 143 , "Dissension Promos" ),
	( 144 , "Dominaria" ),
	( 145 , "Dominaria Promos" ),
	( 146 , "Dominaria Tokens" ),
	( 147 , "Double Masters" ),
	( 148 , "Double Masters Tokens" ),
	( 149 , "Dragon Con" ),
	( 150 , "Dragon's Maze" ),
	( 151 , "Dragon's Maze Promos" ),
	( 152 , "Dragon's Maze Tokens" ),
	( 153 , "Dragons of Tarkir" ),
	( 154 , "Dragons of Tarkir Promos" ),
	( 155 , "Dragons of Tarkir Tokens" ),
	( 156 , "Duel Decks Anthology: Divine vs. Demonic" ),
	( 157 , "Duel Decks Anthology: Divine vs. Demonic Tokens" ),
	( 158 , "Duel Decks Anthology: Elves vs. Goblins" ),
	( 159 , "Duel Decks Anthology: Elves vs. Goblins Tokens" ),
	( 160 , "Duel Decks Anthology: Garruk vs. Liliana" ),
	( 161 , "Duel Decks Anthology: Garruk vs. Liliana Tokens" ),
	( 162 , "Duel Decks Anthology: Jace vs. Chandra" ),
	( 163 , "Duel Decks Anthology: Jace vs. Chandra Tokens" ),
	( 164 , "Duel Decks: Ajani vs. Nicol Bolas" ),
	( 165 , "Duel Decks: Ajani vs. Nicol Bolas Tokens" ),
	( 166 , "Duel Decks: Blessed vs. Cursed" ),
	( 167 , "Duel Decks: Divine vs. Demonic" ),
	( 168 , "Duel Decks: Divine vs. Demonic Tokens" ),
	( 169 , "Duel Decks: Elspeth vs. Kiora" ),
	( 170 , "Duel Decks: Elspeth vs. Tezzeret" ),
	( 171 , "Duel Decks: Elspeth vs. Tezzeret Tokens" ),
	( 172 , "Duel Decks: Elves vs. Goblins" ),
	( 173 , "Duel Decks: Elves vs. Goblins Tokens" ),
	( 174 , "Duel Decks: Elves vs. Inventors" ),
	( 175 , "Duel Decks: Elves vs. Inventors Tokens" ),
	( 176 , "Duel Decks: Garruk vs. Liliana" ),
	( 177 , "Duel Decks: Garruk vs. Liliana Tokens" ),
	( 178 , "Duel Decks: Heroes vs. Monsters" ),
	( 179 , "Duel Decks: Heroes vs. Monsters Tokens" ),
	( 180 , "Duel Decks: Izzet vs. Golgari" ),
	( 181 , "Duel Decks: Izzet vs. Golgari Tokens" ),
	( 182 , "Duel Decks: Jace vs. Chandra" ),
	( 183 , "Duel Decks: Jace vs. Chandra Tokens" ),
	( 184 , "Duel Decks: Jace vs. Vraska" ),
	( 185 , "Duel Decks: Jace vs. Vraska Tokens" ),
	( 186 , "Duel Decks: Knights vs. Dragons" ),
	( 187 , "Duel Decks: Knights vs. Dragons Tokens" ),
	( 188 , "Duel Decks: Merfolk vs. Goblins" ),
	( 189 , "Duel Decks: Merfolk vs. Goblins Tokens" ),
	( 190 , "Duel Decks: Mind vs. Might" ),
	( 191 , "Duel Decks: Mind vs. Might Tokens" ),
	( 192 , "Duel Decks: Mirrodin Pure vs. New Phyrexia" ),
	( 193 , "Duel Decks: Nissa vs. Ob Nixilis" ),
	( 194 , "Duel Decks: Phyrexia vs. the Coalition" ),
	( 195 , "Duel Decks: Phyrexia vs. the Coalition Tokens" ),
	( 196 , "Duel Decks: Sorin vs. Tibalt" ),
	( 197 , "Duel Decks: Sorin vs. Tibalt Tokens" ),
	( 198 , "Duel Decks: Speed vs. Cunning" ),
	( 199 , "Duel Decks: Venser vs. Koth" ),
	( 200 , "Duel Decks: Venser vs. Koth Tokens" ),
	( 201 , "Duel Decks: Zendikar vs. Eldrazi" ),
	( 202 , "Duels of the Planeswalkers" ),
	( 203 , "Duels of the Planeswalkers 2009 Promos " ),
	( 204 , "Duels of the Planeswalkers 2010 Promos " ),
	( 205 , "Duels of the Planeswalkers 2012 Promos " ),
	( 206 , "Duels of the Planeswalkers 2013 Promos " ),
	( 207 , "Duels of the Planeswalkers 2014 Promos " ),
	( 208 , "Duels of the Planeswalkers 2015 Promos " ),
	( 209 , "Eighth Edition" ),
	( 210 , "Eighth Edition Promos" ),
	( 211 , "Eldritch Moon" ),
	( 212 , "Eldritch Moon Promos" ),
	( 213 , "Eldritch Moon Tokens" ),
	( 214 , "Eternal Masters" ),
	( 215 , "Eternal Masters Tokens" ),
	( 216 , "European Land Program" ),
	( 217 , "Eventide" ),
	( 218 , "Eventide Promos" ),
	( 219 , "Eventide Tokens" ),
	( 220 , "Exodus" ),
	( 221 , "Exodus Promos" ),
	( 222 , "Explorers of Ixalan" ),
	( 223 , "Face the Hydra" ),
	( 224 , "Fallen Empires" ),
	( 225 , "Fate Reforged" ),
	( 226 , "Fate Reforged Clash Pack" ),
	( 227 , "Fate Reforged Promos" ),
	( 228 , "Fate Reforged Tokens" ),
	( 229 , "Fifth Dawn" ),
	( 230 , "Fifth Dawn Promos" ),
	( 231 , "Fifth Edition" ),
	( 232 , "Foreign Black Border" ),
	( 233 , "Forgotten Realms Commander" ),
	( 234 , "Fourth Edition" ),
	( 235 , "Fourth Edition Foreign Black Border" ),
	( 236 , "Friday Night Magic 2000" ),
	( 237 , "Friday Night Magic 2001" ),
	( 238 , "Friday Night Magic 2002" ),
	( 239 , "Friday Night Magic 2003" ),
	( 240 , "Friday Night Magic 2004" ),
	( 241 , "Friday Night Magic 2005" ),
	( 242 , "Friday Night Magic 2006" ),
	( 243 , "Friday Night Magic 2007" ),
	( 244 , "Friday Night Magic 2008" ),
	( 245 , "Friday Night Magic 2009" ),
	( 246 , "Friday Night Magic 2010" ),
	( 247 , "Friday Night Magic 2011" ),
	( 248 , "Friday Night Magic 2012" ),
	( 249 , "Friday Night Magic 2013" ),
	( 250 , "Friday Night Magic 2014" ),
	( 251 , "Friday Night Magic 2015" ),
	( 252 , "Friday Night Magic 2016" ),
	( 253 , "Friday Night Magic 2017" ),
	( 254 , "Friday Night Magic 2018" ),
	( 255 , "From the Vault: Angels" ),
	( 256 , "From the Vault: Annihilation" ),
	( 257 , "From the Vault: Dragons" ),
	( 258 , "From the Vault: Exiled" ),
	( 259 , "From the Vault: Legends" ),
	( 260 , "From the Vault: Lore" ),
	( 261 , "From the Vault: Realms" ),
	( 262 , "From the Vault: Relics" ),
	( 263 , "From the Vault: Transform" ),
	( 264 , "From the Vault: Twenty" ),
	( 265 , "Future Sight" ),
	( 266 , "Future Sight Promos" ),
	( 267 , "GRN Guild Kit" ),
	( 268 , "GRN Guild Kit Tokens" ),
	( 269 , "GRN Ravnica Weekend" ),
	( 270 , "Game Night" ),
	( 271 , "Game Night 2019" ),
	( 272 , "Game Night 2019 Tokens" ),
	( 273 , "Gatecrash" ),
	( 274 , "Gatecrash Promos" ),
	( 275 , "Gatecrash Tokens" ),
	( 276 , "Gateway 2006" ),
	( 277 , "Gateway 2007" ),
	( 278 , "Gateway 2008" ),
	( 279 , "Global Series Jiang Yanggu & Mu Yanling" ),
	( 280 , "Grand Prix Promos" ),
	( 281 , "Guildpact" ),
	( 282 , "Guildpact Promos" ),
	( 283 , "Guilds of Ravnica" ),
	( 284 , "Guilds of Ravnica Promos" ),
	( 285 , "Guilds of Ravnica Tokens" ),
	( 286 , "Guru" ),
	( 287 , "Hachette UK" ),
	( 288 , "Happy Holidays" ),
	( 289 , "HarperPrism Book Promos" ),
	( 290 , "HasCon 2017" ),
	( 291 , "Historic Anthology 1" ),
	( 292 , "Historic Anthology 2" ),
	( 293 , "Historic Anthology 3" ),
	( 294 , "Historic Anthology 4" ),
	( 295 , "Historic Anthology 5" ),
	( 296 , "Hobby Japan Promos" ),
	( 297 , "Homelands" ),
	( 298 , "Hour of Devastation" ),
	( 299 , "Hour of Devastation Promos" ),
	( 300 , "Hour of Devastation Tokens" ),
	( 301 , "IDW Comics 2012" ),
	( 302 , "IDW Comics 2013" ),
	( 303 , "IDW Comics 2014" ),
	( 304 , "Ice Age" ),
	( 305 , "Iconic Masters" ),
	( 306 , "Iconic Masters Tokens" ),
	( 307 , "Ikoria: Lair of Behemoths" ),
	( 308 , "Ikoria: Lair of Behemoths Promos" ),
	( 309 , "Ikoria: Lair of Behemoths Tokens" ),
	( 310 , "Innistrad" ),
	( 311 , "Innistrad Promos" ),
	( 312 , "Innistrad Tokens" ),
	( 313 , "Intl. Collectors’ Edition" ),
	( 314 , "Introductory Two-Player Set" ),
	( 315 , "Invasion" ),
	( 316 , "Invasion Promos" ),
	( 317 , "Ixalan" ),
	( 318 , "Ixalan Promos" ),
	( 319 , "Ixalan Tokens" ),
	( 320 , "Japan Junior Tournament" ),
	( 321 , "Journey into Nyx" ),
	( 322 , "Journey into Nyx Hero's Path" ),
	( 323 , "Journey into Nyx Promos" ),
	( 324 , "Journey into Nyx Tokens" ),
	( 325 , "Judge Gift Cards 1998" ),
	( 326 , "Judge Gift Cards 1999" ),
	( 327 , "Judge Gift Cards 2000" ),
	( 328 , "Judge Gift Cards 2001" ),
	( 329 , "Judge Gift Cards 2002" ),
	( 330 , "Judge Gift Cards 2003" ),
	( 331 , "Judge Gift Cards 2004" ),
	( 332 , "Judge Gift Cards 2005" ),
	( 333 , "Judge Gift Cards 2006" ),
	( 334 , "Judge Gift Cards 2007" ),
	( 335 , "Judge Gift Cards 2008" ),
	( 336 , "Judge Gift Cards 2009" ),
	( 337 , "Judge Gift Cards 2010" ),
	( 338 , "Judge Gift Cards 2011" ),
	( 339 , "Judge Gift Cards 2012" ),
	( 340 , "Judge Gift Cards 2013" ),
	( 341 , "Judge Gift Cards 2014" ),
	( 342 , "Judge Gift Cards 2015" ),
	( 343 , "Judge Gift Cards 2016" ),
	( 344 , "Judge Gift Cards 2017" ),
	( 345 , "Judge Gift Cards 2018" ),
	( 346 , "Judge Gift Cards 2019" ),
	( 347 , "Judge Gift Cards 2020" ),
	( 348 , "Judge Gift Cards 2021" ),
	( 349 , "Judgment" ),
	( 350 , "Judgment Promos" ),
	( 351 , "Jumpstart" ),
	( 352 , "Jumpstart Arena Exclusives" ),
	( 353 , "Jumpstart Front Cards" ),
	( 354 , "Junior APAC Series" ),
	( 355 , "Junior Series Europe" ),
	( 356 , "Junior Super Series" ),
	( 357 , "Kaladesh" ),
	( 358 , "Kaladesh Inventions" ),
	( 359 , "Kaladesh Promos" ),
	( 360 , "Kaladesh Remastered" ),
	( 361 , "Kaladesh Tokens" ),
	( 362 , "Kaldheim" ),
	( 363 , "Kaldheim Art Series" ),
	( 364 , "Kaldheim Commander" ),
	( 365 , "Kaldheim Commander Tokens" ),
	( 366 , "Kaldheim Promos" ),
	( 367 , "Kaldheim Tokens" ),
	( 368 , "Khans of Tarkir" ),
	( 369 , "Khans of Tarkir Promos" ),
	( 370 , "Khans of Tarkir Tokens" ),
	( 371 , "League Tokens 2012" ),
	( 372 , "League Tokens 2013" ),
	( 373 , "League Tokens 2014" ),
	( 374 , "League Tokens 2015" ),
	( 375 , "League Tokens 2016" ),
	( 376 , "League Tokens 2017" ),
	( 377 , "Legacy Championship" ),
	( 378 , "Legendary Cube Prize Pack" ),
	( 379 , "Legends" ),
	( 380 , "Legions" ),
	( 381 , "Legions Promos" ),
	( 382 , "Limited Edition Alpha" ),
	( 383 , "Limited Edition Beta" ),
	( 384 , "Lorwyn" ),
	( 385 , "Lorwyn Promos" ),
	( 386 , "Lorwyn Tokens" ),
	( 387 , "Love Your LGS 2020" ),
	( 388 , "Love Your LGS 2021" ),
	( 389 , "M15 Prerelease Challenge" ),
	( 390 , "M19 Gift Pack" ),
	( 391 , "M19 Standard Showdown" ),
	( 392 , "M20 Promo Packs" ),
	( 393 , "MTG Arena Promos" ),
	( 394 , "Magazine Inserts" ),
	( 395 , "Magic 2010" ),
	( 396 , "Magic 2010 Promos" ),
	( 397 , "Magic 2010 Tokens" ),
	( 398 , "Magic 2011" ),
	( 399 , "Magic 2011 Promos" ),
	( 400 , "Magic 2011 Tokens" ),
	( 401 , "Magic 2012" ),
	( 402 , "Magic 2012 Promos" ),
	( 403 , "Magic 2012 Tokens" ),
	( 404 , "Magic 2013" ),
	( 405 , "Magic 2013 Promos" ),
	( 406 , "Magic 2013 Tokens" ),
	( 407 , "Magic 2014" ),
	( 408 , "Magic 2014 Promos" ),
	( 409 , "Magic 2014 Tokens" ),
	( 410 , "Magic 2015" ),
	( 411 , "Magic 2015 Clash Pack" ),
	( 412 , "Magic 2015 Promos" ),
	( 413 , "Magic 2015 Tokens" ),
	( 414 , "Magic Online Avatars" ),
	( 415 , "Magic Online Promos" ),
	( 416 , "Magic Online Theme Decks" ),
	( 417 , "Magic Origins" ),
	( 418 , "Magic Origins Clash Pack" ),
	( 419 , "Magic Origins Promos" ),
	( 420 , "Magic Origins Tokens" ),
	( 421 , "Magic Player Rewards 2001" ),
	( 422 , "Magic Player Rewards 2002" ),
	( 423 , "Magic Player Rewards 2003" ),
	( 424 , "Magic Player Rewards 2004" ),
	( 425 , "Magic Player Rewards 2005" ),
	( 426 , "Magic Player Rewards 2006" ),
	( 427 , "Magic Player Rewards 2007" ),
	( 428 , "Magic Player Rewards 2008" ),
	( 429 , "Magic Player Rewards 2009" ),
	( 430 , "Magic Player Rewards 2010" ),
	( 431 , "Magic Player Rewards 2011" ),
	( 432 , "Magic Premiere Shop 2005" ),
	( 433 , "Magic Premiere Shop 2006" ),
	( 434 , "Magic Premiere Shop 2007" ),
	( 435 , "Magic Premiere Shop 2008" ),
	( 436 , "Magic Premiere Shop 2009" ),
	( 437 , "Magic Premiere Shop 2010" ),
	( 438 , "Magic Premiere Shop 2011" ),
	( 439 , "MagicFest 2019" ),
	( 440 , "MagicFest 2020" ),
	( 441 , "Masters 25" ),
	( 442 , "Masters 25 Tokens" ),
	( 443 , "Masters Edition" ),
	( 444 , "Masters Edition II" ),
	( 445 , "Masters Edition III" ),
	( 446 , "Masters Edition IV" ),
	( 447 , "Mercadian Masques" ),
	( 448 , "Mercadian Masques Promos" ),
	( 449 , "MicroProse Promos" ),
	( 450 , "Mirage" ),
	( 451 , "Mirrodin" ),
	( 452 , "Mirrodin Besieged" ),
	( 453 , "Mirrodin Besieged Promos" ),
	( 454 , "Mirrodin Besieged Tokens" ),
	( 455 , "Mirrodin Promos" ),
	( 456 , "Miscellaneous Book Promos" ),
	( 457 , "Modern Event Deck 2014" ),
	( 458 , "Modern Event Deck 2014 Tokens" ),
	( 459 , "Modern Horizons" ),
	( 460 , "Modern Horizons 1 Timeshifts" ),
	( 461 , "Modern Horizons 2" ),
	( 462 , "Modern Horizons 2 Art Series" ),
	( 463 , "Modern Horizons 2 Promos" ),
	( 464 , "Modern Horizons 2 Tokens" ),
	( 465 , "Modern Horizons Art Series" ),
	( 466 , "Modern Horizons Promos" ),
	( 467 , "Modern Horizons Tokens" ),
	( 468 , "Modern Masters" ),
	( 469 , "Modern Masters 2015" ),
	( 470 , "Modern Masters 2015 Tokens" ),
	( 471 , "Modern Masters 2017" ),
	( 472 , "Modern Masters 2017 Tokens" ),
	( 473 , "Modern Masters Tokens" ),
	( 474 , "Morningtide" ),
	( 475 , "Morningtide Promos" ),
	( 476 , "Morningtide Tokens" ),
	( 477 , "Multiverse Gift Box" ),
	( 478 , "Mystery Booster" ),
	( 479 , "Mystery Booster Playtest Cards" ),
	( 480 , "Mystery Booster Retail Edition Foils" ),
	( 481 , "Mythic Edition" ),
	( 482 , "Mythic Edition Tokens" ),
	( 483 , "Nationals Promos" ),
	( 484 , "Nemesis" ),
	( 485 , "Nemesis Promos" ),
	( 486 , "New Phyrexia" ),
	( 487 , "New Phyrexia Promos" ),
	( 488 , "New Phyrexia Tokens" ),
	( 489 , "Ninth Edition" ),
	( 490 , "Ninth Edition Promos" ),
	( 491 , "Oath of the Gatewatch" ),
	( 492 , "Oath of the Gatewatch Promos" ),
	( 493 , "Oath of the Gatewatch Tokens" ),
	( 494 , "Odyssey" ),
	( 495 , "Odyssey Promos" ),
	( 496 , "Onslaught" ),
	( 497 , "Onslaught Promos" ),
	( 498 , "Open the Helvault" ),
	( 499 , "Planar Chaos" ),
	( 500 , "Planar Chaos Promos" ),
	( 501 , "Planechase" ),
	( 502 , "Planechase 2012" ),
	( 503 , "Planechase 2012 Planes" ),
	( 504 , "Planechase Anthology" ),
	( 505 , "Planechase Anthology Planes" ),
	( 506 , "Planechase Anthology Tokens" ),
	( 507 , "Planechase Planes" ),
	( 508 , "Planeshift" ),
	( 509 , "Planeshift Promos" ),
	( 510 , "Ponies: The Galloping" ),
	( 511 , "Portal" ),
	( 512 , "Portal Demo Game" ),
	( 513 , "Portal Second Age" ),
	( 514 , "Portal Three Kingdoms" ),
	( 515 , "Portal: Three Kingdoms Promos" ),
	( 516 , "Premium Deck Series: Fire and Lightning" ),
	( 517 , "Premium Deck Series: Graveborn" ),
	( 518 , "Premium Deck Series: Slivers" ),
	( 519 , "Pro Tour Collector Set" ),
	( 520 , "Pro Tour Promos" ),
	( 521 , "Promotional Planes" ),
	( 522 , "Promotional Schemes" ),
	( 523 , "Prophecy" ),
	( 524 , "Prophecy Promos" ),
	( 525 , "RNA Guild Kit" ),
	( 526 , "RNA Guild Kit Tokens" ),
	( 527 , "RNA Ravnica Weekend" ),
	( 528 , "Ravnica Allegiance" ),
	( 529 , "Ravnica Allegiance Promos" ),
	( 530 , "Ravnica Allegiance Tokens" ),
	( 531 , "Ravnica: City of Guilds" ),
	( 532 , "Ravnica: City of Guilds Promos" ),
	( 533 , "Redemption Program" ),
	( 534 , "Renaissance" ),
	( 535 , "Resale Promos" ),
	( 536 , "Return to Ravnica" ),
	( 537 , "Return to Ravnica Promos" ),
	( 538 , "Return to Ravnica Tokens" ),
	( 539 , "Revised Edition" ),
	( 540 , "Rinascimento" ),
	( 541 , "Rise of the Eldrazi" ),
	( 542 , "Rise of the Eldrazi Promos" ),
	( 543 , "Rise of the Eldrazi Tokens" ),
	( 544 , "Rivals Quick Start Set" ),
	( 545 , "Rivals of Ixalan" ),
	( 546 , "Rivals of Ixalan Promos" ),
	( 547 , "Rivals of Ixalan Tokens" ),
	( 548 , "Salvat 2005" ),
	( 549 , "Salvat 2011" ),
	( 550 , "San Diego Comic-Con 2013" ),
	( 551 , "San Diego Comic-Con 2014" ),
	( 552 , "San Diego Comic-Con 2015" ),
	( 553 , "San Diego Comic-Con 2016" ),
	( 554 , "San Diego Comic-Con 2017" ),
	( 555 , "San Diego Comic-Con 2018" ),
	( 556 , "San Diego Comic-Con 2019" ),
	( 557 , "Saviors of Kamigawa" ),
	( 558 , "Saviors of Kamigawa Promos" ),
	( 559 , "Scars of Mirrodin" ),
	( 560 , "Scars of Mirrodin Promos" ),
	( 561 , "Scars of Mirrodin Tokens" ),
	( 562 , "Scourge" ),
	( 563 , "Scourge Promos" ),
	( 564 , "Secret Lair Drop" ),
	( 565 , "Secret Lair: Ultimate Edition" ),
	( 566 , "Sega Dreamcast Cards" ),
	( 567 , "Seventh Edition" ),
	( 568 , "Shadowmoor" ),
	( 569 , "Shadowmoor Promos" ),
	( 570 , "Shadowmoor Tokens" ),
	( 571 , "Shadows over Innistrad" ),
	( 572 , "Shadows over Innistrad Promos" ),
	( 573 , "Shadows over Innistrad Tokens" ),
	( 574 , "Shards of Alara" ),
	( 575 , "Shards of Alara Promos" ),
	( 576 , "Shards of Alara Tokens" ),
	( 577 , "Signature Spellbook: Chandra" ),
	( 578 , "Signature Spellbook: Gideon" ),
	( 579 , "Signature Spellbook: Jace" ),
	( 580 , "Starter 1999" ),
	( 581 , "Starter 2000" ),
	( 582 , "Strixhaven Art Series" ),
	( 583 , "Strixhaven Mystical Archive" ),
	( 584 , "Strixhaven: School of Mages" ),
	( 585 , "Strixhaven: School of Mages Promos" ),
	( 586 , "Strixhaven: School of Mages Tokens" ),
	( 587 , "Stronghold" ),
	( 588 , "Stronghold Promos" ),
	( 589 , "Summer Magic / Edgar" ),
	( 590 , "Summer of Magic" ),
	( 591 , "Tarkir Dragonfury" ),
	( 592 , "Tempest" ),
	( 593 , "Tempest Promos" ),
	( 594 , "Tempest Remastered" ),
	( 595 , "Tenth Edition" ),
	( 596 , "Tenth Edition Promos" ),
	( 597 , "Tenth Edition Tokens" ),
	( 598 , "The Dark" ),
	( 599 , "The List" ),
	( 600 , "Theros" ),
	( 601 , "Theros Beyond Death" ),
	( 602 , "Theros Beyond Death Promos" ),
	( 603 , "Theros Beyond Death Tokens" ),
	( 604 , "Theros Hero's Path" ),
	( 605 , "Theros Promos" ),
	( 606 , "Theros Tokens" ),
	( 607 , "Throne of Eldraine" ),
	( 608 , "Throne of Eldraine Promos" ),
	( 609 , "Throne of Eldraine Tokens" ),
	( 610 , "Time Spiral" ),
	( 611 , "Time Spiral Promos" ),
	( 612 , "Time Spiral Remastered" ),
	( 613 , "Time Spiral Remastered Tokens" ),
	( 614 , "Time Spiral Timeshifted" ),
	( 615 , "Torment" ),
	( 616 , "Torment Promos" ),
	( 617 , "Treasure Chest" ),
	( 618 , "Two-Headed Giant Tournament" ),
	( 619 , "URL/Convention Promos" ),
	( 620 , "Ugin's Fate" ),
	( 621 , "Ultimate Box Topper" ),
	( 622 , "Ultimate Masters" ),
	( 623 , "Ultimate Masters Tokens" ),
	( 624 , "Unglued" ),
	( 625 , "Unglued Tokens" ),
	( 626 , "Unhinged" ),
	( 627 , "Unhinged Promos" ),
	( 628 , "Unlimited Edition" ),
	( 629 , "Unsanctioned" ),
	( 630 , "Unsanctioned Tokens" ),
	( 631 , "Unstable" ),
	( 632 , "Unstable Promos" ),
	( 633 , "Unstable Tokens" ),
	( 634 , "Urza's Destiny" ),
	( 635 , "Urza's Destiny Promos" ),
	( 636 , "Urza's Legacy" ),
	( 637 , "Urza's Legacy Promos" ),
	( 638 , "Urza's Saga" ),
	( 639 , "Urza's Saga Promos" ),
	( 640 , "Vanguard Series" ),
	( 641 , "Vintage Championship" ),
	( 642 , "Vintage Masters" ),
	( 643 , "Visions" ),
	( 644 , "War of the Spark" ),
	( 645 , "War of the Spark Promos" ),
	( 646 , "War of the Spark Tokens" ),
	( 647 , "Weatherlight" ),
	( 648 , "Welcome Deck 2016" ),
	( 649 , "Welcome Deck 2017" ),
	( 650 , "Wizards Play Network 2008" ),
	( 651 , "Wizards Play Network 2009" ),
	( 652 , "Wizards Play Network 2010" ),
	( 653 , "Wizards Play Network 2011" ),
	( 654 , "Wizards Play Network 2012" ),
	( 655 , "Wizards Play Network 2021" ),
	( 656 , "Wizards of the Coast Online Store" ),
	( 657 , "World Championship Decks 1997" ),
	( 658 , "World Championship Decks 1998" ),
	( 659 , "World Championship Decks 1999" ),
	( 660 , "World Championship Decks 2000" ),
	( 661 , "World Championship Decks 2001" ),
	( 662 , "World Championship Decks 2002" ),
	( 663 , "World Championship Decks 2003" ),
	( 664 , "World Championship Decks 2004" ),
	( 665 , "World Championship Promos" ),
	( 666 , "World Magic Cup Qualifiers" ),
	( 667 , "Worldwake" ),
	( 668 , "Worldwake Promos" ),
	( 669 , "Worldwake Tokens" ),
	( 670 , "XLN Standard Showdown" ),
	( 671 , "XLN Treasure Chest" ),
	( 672 , "Zendikar" ),
	( 673 , "Zendikar Expeditions" ),
	( 674 , "Zendikar Promos" ),
	( 675 , "Zendikar Rising" ),
	( 676 , "Zendikar Rising Art Series" ),
	( 677 , "Zendikar Rising Commander" ),
	( 678 , "Zendikar Rising Commander Tokens" ),
	( 679 , "Zendikar Rising Expeditions" ),
	( 680 , "Zendikar Rising Minigames" ),
	( 681 , "Zendikar Rising Promos" ),
	( 682 , "Zendikar Rising Substitute Cards" ),
	( 683 , "Zendikar Rising Tokens" ),
	( 684 , "Zendikar Tokens" ),
)

CMCS = (
	(99,"-"),
	(0,"0.0"),
	(1,"1.0"),
	(2,"2.0"),
	(3,"3.0"),
	(4,"4.0"),
	(5,"5.0"),
	(6,"6.0"),
	(7,"7.0"),
	(8,"8.0"),
	(9,"9.0"),
	(10,"10.0"),
	(11,"11.0"),
	(12,"12.0"),
	(13,"13.0"),
	(14,"14.0"),
	(15,"15.0"),
	(16,"16.0"),

)

CMC_MOD = (
	(1,"="),
	(2,"\u2265"),
	(3,"\u2264"),
	(4,">"),
	(5,"<")
)
class AdvancedSearch(forms.Form):

	colors = forms.MultipleChoiceField(
		choices=COLORS,
		label="Colors:",
		required=False,
		widget=forms.CheckboxSelectMultiple,
		)
	colors_options = forms.ChoiceField(
		choices =XORS,
		label="Colors Modifier:",
		required=False,
		widget=forms.Select(choices=XORS)
		)
	toughness_equality = forms.ChoiceField(
		choices =TOUGHNESS_MOD,
		label="Toughness:",
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
		label="Power:",
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
		label="Artist:",
		required=False,
		)
	rarity = forms.ChoiceField(
		choices = RARITY,
		label="Rarity:",
		required=False,
		widget=forms.Select(choices=RARITY)
		)
	s_name = forms.ChoiceField(
		choices = SETS,
		label="Sets:",
		required=False,
		widget=forms.Select(choices=SETS)
		)
	cmc_equality = forms.ChoiceField(
		choices = CMC_MOD,
		label="Cmc:",
		required=False,
		widget=forms.Select(choices=CMC_MOD)
		)
	cmc_q = forms.ChoiceField(
		choices = CMCS,
		label="",
		required=False,
		widget=forms.Select(choices=CMCS)
		)