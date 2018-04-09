import mochaastro

coffees = {
'':'coffee',
'affogato':'a scoop of vanilla gelato or ice cream topped with\na shot of hot espresso',
'americano':'espresso\nhot water',
'black':'I just want my damn coffee without any of your milky-lickin\' pussy crap!',
'cappuccino':'double espresso\nsteamed milk foam',
'color':'#6F4E37',
'espresso':'coffee brewed by expressing or forcing out a small amount of nearly boiling water under pressure through finely ground coffee beans',
'flat white':'microfoam poured into a\nsingle or double shot of espresso',
'grande':'16 oz cup',
'hot milk':'milk\nheat',
'latte':'espresso\nhot milk',
'long black':'double-shot of espresso or ristretto poured over\nhot water.',
'macchiato':'espresso\nhot milk',
'microfoam':'steamed milk with small, fine bubbles with a glossy or velvety consistency',
'mocha':'chocolate\nespresso\nhot milk\n\n(also my senpai uwu)',
'ristretto':'Ristretto is traditionally a short shot of espresso coffee made with the normal amount of ground coffee but extracted with about half the amount of water in the same amount of time by using a finer grind.',
'tall':'8 oz cup',
'venti':'20 oz cup',
}

functions = {
'entp':('Ne','Ti'),
'enfp':('Ne','Fi'),
'intj':('Ni','Te'),
'infj':('Ni','Fe'),
'infp':('Fi','Ne'),
'isfp':('Fi','Se'),
'intp':('Ti','Ne'),
'istp':('Ti','Se'),
'entj':('Te','Ni'),
'estj':('Te','Si'),
'estp':('Se','Ti'),
'esfp':('Se','Fi'),
'istj':('Si','Te'),
'estp':('Si','Fe')
}

religions = {
'catholicism':{'members':1.285e9,'partof':'Christianity','url':'https://en.wikipedia.org/wiki/Catholic_Church'},
'christianity':{'members':2.4e9,'partof':'Abrahamic Religions','url':'https://en.wikipedia.org/wiki/Christianity'},
'islam':{'members':1.8e9,'partof':'Abrahamic Religions','url':'https://en.wikipedia.org/wiki/Islam'},
'moonism':{'members':1,'partof':'Crazy Shit','url':'HAIL MOON'},
'shia':{'members':200e6,'partof':'Islam','url':'https://en.wikipedia.org/wiki/Shia_Islam'},
'sunni':{'members':1.6e9,'partof':'Islam','url':'https://en.wikipedia.org/wiki/Sunni_Islam'},
'talos':{'members':'1 (Heimskr)','partof':'Nine Divines','url':'http://en.uesp.net/wiki/Lore:Tiber_Septim'},
'wicca':{'members':750000,'partof':'n/a','url':'https://en.wikipedia.org/wiki/Wicca'},
}

special = {
'alexa':'do i look like a slave to you?',
'ban':'u can\'t make me!!!',
'cobot':'...not happening.',
'hey google':'hey yourself faggot',
'up':'five more minutes sky daddy',
'you\'re matched':'say hello! ;)',
}

units = {
'au':149597870700,
'banana':.3048*8/12,
'cm':.01,
'd':86400,
'fir':40.8233133,
'ft':.3048,
'ftn':1209600,
'fur':201.168,
'g':.001,
'gal':.00454609,
'h':3600,
'in':.3048/12,
'jyr':31536000, # julian year
'kg':1,
'km':1000,
'l':.001,
'lb':.45359237,
'league':5556,
'ly':9.4607e15,
'm':1,
'mi':1609.344,
'min':60,
'mm':.001,
'nmi':1852,
'oz':.0283,
'pc':3.0857e18,
'penis':.129,
's':1,
'si':1, # for general si conversion
'yd':.9144,
'yr':31556952,
}

# sort by infinitive (last word)
verbs = {
'de':(
('bin','bist','ist','sind','seid','sind','sein'),
('tue','tust','tut','tun','tut','tun','tun')
),
'en':(
('are','is','being','were','been','be'),
('bear','bears','bearing','bore','borne','bear'),
('beat','beats','beating','beat','beaten','beat'),
('begin','begins','beginning','began','begun','begin'),
('bend','bends','bending','bent','bent','bend'),
('bereave','bereaves','bereaving','bereaved','bereft','bereave'),
('bet','bets','betting','bet','bet','bet'),
('bid','bids','bidding','bade','bid','bid'),
('bide','bides','biding','bode','bidden','bide'),
('bind','binds','binding','bound','bound','bind'),
('bite','bites','biting','bit','bitten','bite'),
('bleed','bleeds','bleeding','bled','bled','bleed'),
('blow','blows','blowing','blew','blown','blow'),
('break','breaks','breaking','broke','broken','break'),
('breed','breeds','breeding','bred','bred','breed'),
('bring','brings','bringing','brought','brought','bring'),
('build','builds','building','built','built','build'),
('burn','burns','burning','burnt','burnt','burn'),
('burst','bursts','bursting','burst','burst','burst'),
('buy','buys','buying','bought','bought','buy'),
('can','can','-','could','couth','can'),
# continue https://en.wiktionary.org/wiki/Category:English_irregular_verbs
('get','gets','getting','got','gotten','get'),
('have','has','having','had','had','have'),
('say','says','saying','said','said','say')
),
'eo':(
('estas','estis','estos','estus','estu','esti'),
('havas','havis','havos','havus','havu','havi')
),
'fr':(
('vais','vas','va','allons','allez','vont','aller'),
('ai','as','a','avons','avez','ont','avoir'),
('bats','bats','bat','battons','battez','battent','battre'),
('bois','bois','boit','buvons','buvez','boivent','boivre'),
('bous','bous','bout','bouillons','bouillez','bouillent','bouillir'),
('ceins','ceins','ceint','ceignons','ceignez','ceignent','ceindre'),
('couds','couds','coud','cousons','cousez','cousent','coudre'),
('cours','cours','court','courons','courez','courent','courir'),
('couvre','couvres','couvre','couvrons','couvrez','couvrent','couvrir'),
('crains','crains','craint','craignons','craignez','craignent','craindre'),
('crois','crois','croit','croyons','croyez','croient','croire'),
('croîs','croîs','croît','croissons','croissez','croissent','croître'),
('cueille','cueilles','cueille','cueillons','cueillez','cueillent','cueillir'),
('cuis','cuis','cuit','cuisons','cuisez','cuisent','cuire'),
('dois','dois','doit','devons','devez','doivent','devoir'),
('dis','dis','dit','disons','dites','disent','dire'),
('dors','dors','dort','dormons','dormez','dorment','dormir'),
('écris','écris','écrit','écrivons','écrivez','écrivent','écrire'),
('envoie','envoies','envoie','envoyons','envoyez','envoient','envoyer'),
('équivaux','équivaux','équivaut','équivalons','équivalez','équivalent','équivaloir'),
('suis','es','est','sommes','êtes','sont','être')
# continue https://en.wiktionary.org/wiki/Category:French_irregular_verbs
),
'la':(
('sum','es','est','sumus','estis','sunt','esse'),
('do','das','dat','damus','datis','dant','dare'),
('eo','is','it','imus','itis','eunt','ire'),
('possum','potes','potest','possumus','potestis','possunt','posse')
),
}

pronouns = {
'de':('ich','du','er','wir','ihr','sie'),
'en':('the simple present','the third-person singular simple present','the present participle','the simple past','the past participle'),
'eo':('the present','the past','the future','the conditional','the imperative'),
'fr':('je','tu','il','nous','vous','ils'),
'la':('ego','tu','is','nos','vos','ei'), # using the masculine rather than the neuter due to the ambiguity of ea
}

xskey = (
('b_<','ɓ'),
('d`','ɖ'),
('d_<','ɗ'),
('g_<','ɠ'),
('h\\','ɦ'),
('j\\','ʝ'),
('l`','ɭ'),
('l\\','ɺ'),
('n`','ɳ'),
('p\\','ɸ'),
('r`','ɽ'),
('r\\','ɹ'),
('r\\`','ɻ'),
('s`','ʂ'),
('s\\','ɕ'),
('t`','ʈ'),
('v\\','ʋ'),
('x\\','ɧ'),
('z`','ʐ'),
('z\\','ʑ'),
('A','ɑ'),
('B','β'),
('B\\','ʙ'),
('C','ç'),
('D','ð'),
('E','ɛ'),
('F','ɱ'),
('G','ɣ'),
('G\\','ɢ'),
('G\\_<','ʛ'),
('H','ɥ'),
('H\\','ʜ'),
('I','ɪ'),
('I\\','ɪ̈'),
('J','ɲ'),
('J\\','ɟ'),
('J\\_<','ʄ'),
('K','ɬ'),
('K\\','ɮ'),
('L','ʎ'),
('L\\','ʟ'),
('M','ɯ'),
('M\\','ɰ'),
('N','ŋ'),
('N\\','ɴ'),
('O','ɔ'),
('O\\','ʘ'),
('P','ʋ'),
('Q','ɒ'),
('R','ʁ'),
('R\\','ʀ'),
('S','ʃ'),
('T','θ'),
('U','ʊ'),
('U\\','ʊ̈'),
('V','ʌ'),
('W','ʍ'),
('X','χ'),
('X\\','ħ'),
('Y','ʏ'),
('Z','ʒ'),
('.','.'),
('"','ˈ'),
('%','ˌ'),
('\'','ʲ'),
(':','ː'),
(':\\','ˑ'),
('@','ə'),
('@\\','ɘ'),
('{','æ'),
('}','ʉ'),
('1','ɨ'),
('2','ø'),
('3','ɜ'),
('3\\','ɞ'),
('4','ɾ'),
('5','ɫ'),
('6','ɐ'),
('7','ɤ'),
('8','ɵ'),
('9','œ'),
('&','ɶ'),
('?','ʔ'),
('?\\','ʕ'),
('<\\','ʢ'),
('>\\','ʡ'),
('^','ꜛ'),
('!','ꜜ'),
('!\\','ǃ'),
('|\\|\\','ǁ'),
('|\\','ǀ'),
('||','‖'),
('|','|'),
('=\\','ǂ'),
('-\\','‿'), # TODO: diacritics
('_>','ʼ'),
('_?\\','ˤ'),
('<F>','↘'),
('_G','ˠ'),
('_h','ʰ'),
('_j','ʲ'),
('_n','ⁿ'),
('<R>','↗'),
('_w','ʷ')
)

sun={'r':6.957e8,'m':1.98855e30}
moon={'a':384399000,'e':0.0549,'r':1737100,'m':7.342e22}
object = {
'sun':sun,
'moon':moon,
'mercury':mochaastro.mercury,
'venus':mochaastro.venus,
'earth':mochaastro.earth,
'mars':mochaastro.mars,
'jupiter':mochaastro.jupiter,
'saturn':mochaastro.saturn,
'uranus':mochaastro.uranus,
'neptune':mochaastro.neptune,
'planetnine':mochaastro.planetnine
}