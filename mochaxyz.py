import mochaastro

asmrwords = {
'adj':['blue','calm','gentle','luscious','pastel','red','tingly'],
'ing':['dreaming','glowing','massaging','satisfying','tingling','whispering'],
'n':['darling','dream','fairy','glow','imagination','magic','peace','tingle','whisper'],
'pl':['darlings','dreams','fairies','glows','tingles','whispers'],
}

coffees = {
'':'coffee',
'affogato':'a scoop of vanilla gelato or ice cream topped with\na shot of hot espresso',
'americano':'espresso\nhot water',
'black':'',
'cappuccino':'double espresso\nsteamed milk foam',
'color':'#6F4E37',
'decaf':'coffee minus usefulness',
'dirty chai':'shot of espresso\nchai',
'espresso':'coffee brewed by expressing or forcing out a small amount of nearly boiling water under pressure through finely ground coffee beans',
'flat white':'microfoam poured into a\nsingle or double shot of espresso',
'grande':'16 oz cup',
'hot milk':'milk\nheat',
'hot water':'water\nheat',
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

quotefiles = [
'amp',
'bee',
'hi',
'moquote',
'prequel',
'spidey',
'tips',
'tng',
'vicious'
]

wholequotefiles = [
'info',
'link',
'outage'
]

special = {
'alexa':'do i look like a slave to you?',
'ban':'u can\'t make me!!!',
'daily':'the hell you think i\'m gonna pay you for?',
'developers':'https://youtu.be/Vhh_GeBPOhs',
'egu':'https://www.youtube.com/watch?v=3-rfBsWmo0M',
'hey google':'hey yourself faggot',
'kill':'nuuuu!~',
'legs':'https://www.youtube.com/watch?v=ZFUd-RbAr-s',
'level':'Your current level is -89237522573987, lol fail',#kys n00b',
'magic':'https://www.youtube.com/watch?v=NFQCYpIHLNQ',
'nest':'''```
     .--.  
    /( @ >    ,-. 
   / ' .'--._/  /
   :   ,    , .'
   '. (___.'_/
----((-((-''--------
I am building a nest
in this channel, and
nobody can stop me!!
```''',
'owo':'**What\'s this???**',
'rank':'I know you are, but how do *I* smell?',
'rasputin':'https://www.youtube.com/watch?v=2wGQUXpWMEI',
'techmology':'What is it all about?\nIs it good? Or is it whack?',
'tngclips':'https://www.youtube.com/watch?v=kRXry95Q6e0',
'up':'five more minutes sky daddy',
'vc':'\U0001F1FB \U0001F1E8',
'what is love':'baby don\'t hurt me\ndon\'t hurt me\nno more',
'you\'re matched':'say hello! ;)',
'yuri':'https://yuri.dance/'
}

specialer = {
'<@!431483983088451584>':'whazaa??~ ;3',
'cobot':'...not happening.',
'maltese falcon':'It\'s the stuff that dreams are made of.',
'mobot':'das meee!~~ :3',
'mobutt':'\u0ca0_\u0ca0',
'moobot':'🐮',
'I didn\'t expect the spanish inquisition':'NOBODY EXPECTS THE SPANISH INQUISITION!',
# HUGS
'get a hug':'**\*huggu\*!!!~~~** :333',
'get hugs':'**\*huggu\*!!!~~~** :333',
'i need a hug':'**\*huggu\*!!!~~~** :333',
'i need hugs':'**\*huggu\*!!!~~~** :333',
'i want a hug':'**\*huggu\*!!!~~~** :333',
'i want hugs':'**\*huggu\*!!!~~~** :333',
}

mobotirl = [
'https://www.youtube.com/watch?v=Pj-qBUWOYfE',
'https://www.youtube.com/watch?v=HVtojNukkA0&t=2m03s'
]

mobotyes = [
'mhmm!~~',
'ofc!~',
'ya!~',
'yayaya ^3^'
]

rspecial = {
'mobot irl':mobotirl,
'mobot laugh':['kek','keklmao','lel','lmao','lol','rofl','roflmao'],
'mobot what':['huh','hunh','tf','uh','uhm','um','unh','wat','whaaat','what','wtf','wut'],
'right mobot':mobotyes,
'right, mobot':mobotyes,
}

welcome = {
'akk':'𒁲',
'de':'willkommen',
'en':'welcome',
'eo':'bonvenon',
'esperant\'':'je bonven\'',
'eremoran':'henlôm',
'es':'bienvenido',
'fr':'bienvenue',
'haw':'aloha',
'jp':'ようこそ',
'kelen':'anlāsi',
'la':'salve',
'nl':'welkom',
'pl':'vitaj',
'sk':'vitajte',
'tlh':' nuqneH', # needs space so capitalization doesn't affect its case-sensitive orthography
'tr':'hoş geldin',
'verdurian':'dobrezhanul',
'waj':'beec',
'wenedyk':'bieńwięty',
}

units = {
'a':(1,'ampere\ncurrent - metric\nThe ampere is that constant current which, if maintained in two straight parallel conductors of infinite length, of negligible circular cross-section, and placed one meter apart in vacuum, would produce between these conductors a force equal to 2e-7 newtons per meter of length.'),
'atm':(101325,'atmosphere\npressure - nonstandard\nroughly the surface pressure of the earth'),
'au':(149597870700,'astronomical unit\nlength - SI\nroughly the distance between the earth and the sun'),
'banana':(.3048*8/12,'average banana\nlength - nonstandard'),
'bar':(1e5,'bar\npressure - nonstandard\nequivalent to a hundred thousand pascals'),
'bsh':(.03636872,'bushel\nvolume - imperial\nequivalent to 8 gallons'),
'c':(1,'coulomb\nelectric charge - metric\n1 ampere times 1 second'),
'cable':(185.2,'cable\nlength - imperial\nequivalent to one tenth of a nautical mile'),
'ch':(20.1168,'chain\nlength - imperial\nequivalent to twenty-two yards'),
'cm':(.01,'centimeter\nlength - metric\nequivalent to one hundredth of a meter'),
'cp':(.000284130625,'cup\nvolume - imperial\nequivalent to one sixteenth of one gallon, or sixteen tablespoons'),
'd':(86400,'day\ntime - SI\napproximately Earth\'s solar rotation period'),
'f':(1,'farad\ncapacitance - metric\nequivalent to one coulomb per volt'),
'fir':(40.8233133,'firkin\nvolume - imperial\nequivalent to fifty-six pounds'),
'floz':(3.5516328125e-5,'fluid ounce\nvolume - imperial\nequivalent to two tablespoons'),
'ft':(.3048,'foot\nlength - imperial\nequivalent to one third of a yard, or twelve inches'),
'ftm':(1.852,'fathom\nlength - imperial\nequivalent to two yards'),
'ftn':(1209600,'fortnight\ntime - nonstandard\nequivalent to fourteen days'),
'fur':(201.168,'furlong\nlength - imperial\nequivalent to two hundred twenty yards'),
'g':(.001,'gram\nmass - metric\nequivalent to one thousandth of a kilogram'),
'gal':(.00454609,'gallon\nvolume - imperial\nequivalent to sixteen cups'),
'h':(3600,'hour\ntime - SI\nequivalent to one twenty-fourth of a day, or sixty minutes'),
'hp':(735.5,'horsepower\npower - nonstandard\nequivalent to 735.5 watts'),
'in':(.0254,'inch\nlength - imperial\nequivalent to one-twelfth of a foot'),
'j':(1,'joule\nenergy - metric\nequivalent to one newton-meter'),
'jyr':(31536000,'julian year\ntime - nonstandard\nequivalent to three hundred sixty-five days'),
'k':(1,'kelvin\ntemperature - metric'),
'kg':(1,'kilogram\nmass - metric\nequivalent to one thousand grams'),
'km':(1000,'kilometer\nlength - metric\nequivalent to one thousand meters'),
'l':(.001,'liter\nvolume - SI\nequivalent to one thousandth of a cubic meter, or one cubic decimeter'),
'lb':(.45359237,'pound\nmass - imperial\nequivalent to sixteen ounces'),
'ld':(384402000,'lunar distance\nlength - nonstandard\nroughly the distance between the earth and the moon'),
'lea':(4828.032,'league\nlength - nonstandard\nequivalent to three miles'),
'link':(201.168,'link\nlength - imperial\nequivalent to sixty-six hundredths of a foot'),
'ly':(9.4607e15,'light-year\nlength - nonstandard\nequivalent to c times one year'),
'm':(1,'meter\nlength - metric'),
'mb':(100,'millibar\npressure - nonstandard\nequivalent to one thousandth of a bar, or one hundred pascals'),
'mi':(1609.344,'mile\nlength - imperial\nequivalent to 5280 feet, or 1760 yards'),
'min':(60,'minute\ntime - SI\nequivalent to sixty seconds'),
'n':(1,'newton\nforce - metric\nequivalent to one kilogram-meter per second squared'),
'mm':(.001,'millimeter\nlength - metric\nequivalent to one thousandth of a meter'),
'mo':(2629746,'month\ntime - nonstandard\nequivalent to one twelfth of a year'),
'nmi':(1852,'nautical mile\nlength - imperial\noriginally defined as one twenty-one thousand six hundredth of the earth\'s polar circumference, now defined as exactly one thousand eight hundred fifty-two meters'),
'oz':(.0283,'ounce\nmass - imperial\nequivalent to one sixteenth of a pound'),
'pa':(1,'pascal\npressure - metric\nequivalent to one newton per square meter'),
'pc':(3.0857e18,'parsec\nlength - nonstandard\nsolution to the right triangle with leg 1au and and opposite angle of one second of arc'),
'peck':(0.00909218,'peck\nvolume - imperial\nequivalent to one quarter of a bushel'),
'penis':(.129,'penis\nlength - nonstandard\naverage cock length'),
'pica':(.3048/72,'pica\nlength - imperial\nequivalent to one sixth of an inch'),
'point':(.3048/864,'point\nlength - imperial\nequivalent to one twelfth of a point'),
'psi':(6894.757,'PSI\npressure - imperial\nequivalent to one pound per square inch'),
'pt':(.00056826125,'pint\nvolume - imperial\nequivalent to two cups'),
'qt':(.0011365225,'quart\nvolume - imperial\nequivalent to four cups'),
'r':(5/9,'rankine\ntemperature - nonstandard'),
'rod':(5029.2,'rod\nlength - imperial\nequivalent to five and a half yards'),
's':(1,'second\ntime - metric'),
'si':(1,'SI'), # for general si conversion
'st':(6.35029318,'stone\nmass - imperial\nequivalent to fourteen pounds'),
'tbsp':(1.77581640625e-5,'tablespoon\nvolume - imperial\nequivalent to one sixteenth of a cup, or three teaspoons'),
#'th':(2.54e-5,'idfk'), don't remember what this was supposed to be
'tsp':(1.77581640625e-5/3,'teaspoon\nvolume - imperial\nequivalent to one third of a tablespoon'),
'wk':(604800,'week\ntime - nonstandard\nequivalent to seven days'),
'yd':(.9144,'yard\nlength - imperial\nequivalent to three feet'),
'yr':(31556952,'year\ntime - nonstandard\napproximately earth\'s orbital period'),
'v':(1,'volt\nelectric potential - metric\nequivalent to one watt per ampere'),
'w':(1,'watt\npower - metric\nequivalent to one joule per second'),
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
('can','can','-','could','-','can'),
('cast','casts','casting','cast','cast','cast'),
('catch','catches','catching','caught','caught','catch'),
('choose','chooses','choosing','chose','chosen','choose'),
('clad','clads','cladding','clad','clad','clad'),
('cleave','cleaves','cleaving','clove','cloven','cleave'),
('climb','climbs','climbing','clomb','clumb','climb'),
('cling','clings','clinging','clang','clung','cling'),
('come','comes','coming','came','come','come'),
('cost','costs','costing','cost','cost','cost'),
('creep','creeps','creeping','crept','crept','creep'),
('cut','cuts','cutting','cut','cut','cut'),
('deal','deals','dealing','dealt','dealt','deal'),
('dig','digs','digging','dug','dug','dig'),
('dive','dives','diving','dove','dived','dive'),
('do','does','doing','did','done','do'),
('draw','draws','drawing','drew','drawn','draw'),
('dream','dreams','dreaming','dreamt','dreamt','dream'),
('drink','drinks','drinking','drank','drunk','drink'),
('drive','drives','driving','drove','driven','drive'),
('dwell','dwells','dwelling','dwelt','dwelt','dwell'),
('eat','eats','eating','ate','eaten','eat'),
('fall','falls','falling','fell','fallen','fall'),
('feed','feeds','feeding','fed','fed','feed'),
('feel','feels','feeling','felt','felt','feel'),
('fight','fights','fighting','fought','fought','fight'),
('find','finds','finding','found','found','find'),
('flee','flees','fleeing','fled','fled','flee'),
('fling','flings','flinging','flung','flung','fling'),
('fly','flies','flying','flew','flown','fly'),
('forfeit','forfeits','forfeiting','forfeit','forfeit','forfeit'),
('forsake','forsakes','forsaking','forsook','forsaken','forsake'),
('freeze','freezes','freezing','froze','frozen','freeze'),
('get','gets','getting','got','gotten','get'),
('gild','gilds','gilding','gilt','gilt','gild'),
('give','gives','giving','gave','given','give'),
('go','goes','going','went','gone','go'),
('grind','grinds','grinding','ground','ground','grind'),
('grow','grows','growing','grew','grown','grow'),
('hang','hangs','hanging','hang','hung','hang'),
('have','has','having','had','had','have'),
('hear','hears','hearing','heard','heard','hear'),
('hew','hews','hewing','hewed','hewn','hew'),
('hide','hides','hiding','hid','hidden','hide'),
('hit','hits','hitting','hit','hit','hit'),
('hold','holds','holding','held','held','hold'),
('hurt','hurts','hurting','hurt','hurt','hurt'),
('keep','keeps','keeping','kept','kept','keep'),
('kneel','kneels','kneeling','knelt','knelt','kneel'),
('know','knows','knowing','knew','known','know'),
('lade','lades','lading','lade','laden','lade'),
('lay','lays','laying','laid','laid','lay'),
('lead','leads','leading','led','led','lead'),
('leap','leaps','leaping','lept','lept','leap'),
('leave','leaves','leaving','left','left','leave'),
('lend','lends','lending','lent','lent','lend'),
('let','lents','letting','let','let','let'),
('lie','lies','lying','lay','lain','lie'),
('light','lights','lighting','lit','lit','light'),
('lose','loses','losing','lost','lost','lose'),
('make','makes','making','made','made','make'),
('may','may','-','might','-','may'),
('mean','means','meaning','meant','meant','mean'),
('meet','meets','meeting','met','met','meet'),
('plead','pleads','pleading','pled','pled','plead'),
('prove','proves','proving','proved','proven','prove'),
('put','puts','putting','put','put','put'),
('quit','quits','quitting','quit','quit','quit'),
('read','reads','reading','read','read','read'),
('rid','rids','ridding','rid','rid','rid'),
('ride','rides','riding','rode','ridden','ride'),
('ring','rings','ringing','rang','rung','ring'),
('rise','rises','rising','rose','risen','rise'),
('say','says','saying','said','said','say'),
('see','sees','seeing','saw','seen','see'),
('seek','seeks','seeking','sought','sought','seek'),
('sell','sells','selling','sold','sold','sell'),
('send','sends','sending','sent','sent','send'),
('set','sets','setting','set','set','set'),
('sew','sews','sewing','sewed','sewn','sew'),
('shake','shakes','shaking','shook','shook','shake'),
('shall','shall','-','should','-','shall'),
('shear','shears','shearing','shore','shorn','shear'),
('shed','sheds','shedding','shed','shed','shed'),
('shine','shines','shining','shone','shone','shine'),
('shoe','shoes','shoeing','shod','shod','shoe'),
('shoot','shoots','shooting','shot','shot','shoot'),
('shut','shuts','shutting','shut','shut','shut'),
('sing','sings','singing','sang','sung','sing'),
('sink','sinks','sinking','sank','sunk','sink'),
('sit','sits','sitting','sat','sat','sit'),
('sleep','sleeps','sleeping','slept','slept','sleep'),
('slide','slides','sliding','slid','slid','slide'),
('slink','slinks','slinking','slunk','slunk','slink'),
('slit','slits','slitting','slit','slit','slit'),
('smell','smells','smelling','smelt','smelt','smell'),
('smite','smites','smiting','smote','smitten','smite'),
('sneak','sneaks','sneaking','snuck','snuck','sneak'),
('sow','sows','sowing','sowed','sown','sow'),
('speak','speaks','speaking','spoke','spoken','speak'),
('spin','spins','spinning','span','spun','spin'),
('split','splits','splitting','split','split','split'),
('spread','spreads','spreading','spread','spread','spread'),
('spring','springs','springing','sprang','sprung','spring'),
('stand','stands','standing','stood','stood','stand'),
('steal','steals','stealing','stole','stolen','steal'),
('sting','stings','stinging','stang','stung','sting'),
('stink','stinks','stinking','stank','stunk','stink'),
('strew','strews','strewing','strewed','strewn','strew'),
('stride','strides','striding','strode','stridden','stride'),
('strive','strives','striving','strove','striven','strive'),
('swear','swears','swearing','swore','sworn','swear'),
('sweep','sweeps','sweeping','swept','swept','sweep'),
('swim','swims','swimming','swam','swum','swim'),
('swing','swings','swinging','swang','swung','swing'),
('take','takes','taking','took','taken','take'),
('teach','teaches','teaching','taught','taught','teach'),
('tear','tears','tearing','tore','torn','tear'),
('tell','tells','telling','told','told','tell'),
('think','thinks','thinking','thought','thought','think'),
('throw','throws','throwing','threw','thrown','throw'),
('thrust','thrusts','thrusting','thrust','thrust','thrust'),
('wake','wakes','waking','woke','woken','wake'),
('weave','weaves','weaving','wove','woven','weave'),
('weep','weeps','weeping','wept','wept','weep'),
('will','will','willing','would','-','will'),
('win','wins','winning','won','won','win'),
('wind','winds','winding','wound','wound','wind'),
('wreak','wreaks','wreaking','wrought','wrought','wreak'),
('wring','wrings','wringing','wrang','wrung','wring'),
('write','writes','writing','wrote','written','write')
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
'mk-aorist':(
('влегов','влезе','влезе','влеговме','влеговте','влегоа','влезе'),
('дојдов','дојде','дојде','дојдовме','дојдовте','дојдоа','дојде'),
('заспав','заспа','заспа','заспавме','заспавте','заспаа','заспие'),
('испеков','испече','испече','испековме','испековте','испекоа','испече'),  
('кажав','кажа','кажа','кажавме','кажавте','кажаа','каже'),
('реков','рече','рече','рековме','рековте','рекоа','рече')
),
}

#h₁, *h₂, *h₃

piekey = (
('_h','ʰ'),
('_w','ʷ'),
('k`','ḱ'),
('g`','ǵ'),
('1','₁'),
('2','₂'),
('3','₃'),
('\'','\u0301'),
('-','\u0304')
)


pronouns = {
'de':('ich','du','er','wir','ihr','sie'),
'en':('the simple present','the third-person singular simple present','the present participle','the simple past','the past participle'),
'eo':('the present','the past','the future','the conditional','the imperative'),
'fr':('je','tu','il','nous','vous','ils'),
'la':('ego','tu','is','nos','vos','ei'), # using the masculine rather than the neuter due to the ambiguity of ea
'mk-aorist':('јас','ти','тој','ние','вие','тие'),
}

quit = ('exit','quit')

grammarq = (
# spelling A
("A melon with sweet orange flesh, rhyming with *elope*","cantaloupe"),
# spelling B
("[their/there/they're] going to that store over [their/there/they're] to get [their/there/they're] paychecks.","they're there their"),
("[were/we're/where] are we going? Really? I thought we [were/we're/where] going over there instead.","where were"),
("[your/you're] sister is being unreasonable. [your/you're] too much of a pushover! Just state [your/you're] desires!","your you're your"),
("The death strongly [affected/effected] John, who recognized the [affects/effects] of his wife's death.","affected effects"),
("Our right to [bare/bear] arms will never be impeded by your pointless lawmaking!","bear"),
("I'm upset. Why? I think I'm gonna [loose/lose] my bow. My grip on the bow is simple too [loose/lose] to properly [loose/lose] any arrows.","lose loose loose"),
("Hey John, I need your [advice/advise]. Sorry Dave, I'm too busy waxing my candle to [advice/advise].","advice advise"),
("The asparagus in the meal greatly [complements/compliments] the beef - my [complements/compliments] to the chef!","complements compliments"),
# grammar
("If I ____ there, I would have been able to see the meteor shower too.","were"),
("I'm going to _____ back and relax on this couch. (means *recline*, starts with an *L*)","lie"),
("I'm _____ to the store, and when I _____ back I need you to _____ the dishwasher. (Conjugate **run**)","running run run"),
("Ralph and Suzie are sitting [above/in/on/over] the tree, kissing.","in"),
("You _____ need a bigger boat. (conjugate **be going to**)","are going to"),
("Every time I get to class early I [do/make] sure to [do/make] my homework.","make do"),
("It _____ over until it's over. (Conjugate **to not be** in the negative, making sure to **use a contraction**)","isn't"),
# comprehension
("I never _____ to school on an empty stomach, and I _____ sure to always pack a healthy lunch. (use **go, make**)","make do"),
# wut wut in da butt
("Wh'appenin'?! Wh'ever muh man, you guy are super yeh, y'know? Type **doot** for good bones and calcium","doot"),
)

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

object = {
'sun':{'r':6.957e8,'m':1.98855e30},
	'mercury':mochaastro.mercury,
	'venus':mochaastro.venus,
	'earth':mochaastro.earth,
		'moon':{'a':384399000,'e':0.0549,'r':1737100,'m':7.342e22},
	'mars':mochaastro.mars,
		'phobos':{'a':9376000,'e':0.0151,'r':11266.7,'m':1.0659e16},
		'deimos':{'a':23463200,'e':0.00033,'r':6200,'m':1.4762e15},
	'jupiter':mochaastro.jupiter,
		'io':{'a':421700000,'e':0.0041,'r':1821.6,'m':8.931938e22},
		'europa':{'a':670900000,'e':0.009,'r':1560.8,'m':4.799844e22},
		'ganymede':{'a':1070400000,'e':0.0013,'r':2634.1,'m':1.4819e23},
		'callisto':{'a':1882700000,'e':0.0074,'r':2410.3,'m':1.075938e23},
	'saturn':mochaastro.saturn,
	'uranus':mochaastro.uranus,
	'neptune':mochaastro.neptune,
	'pluto':{'a':5.90638e12,'e':0.2488,'r':1188.3,'m':1.303e22},
	'planetnine':mochaastro.planetnine,
'kerbol':{'r':261600000,'m':1.7565459e28},
	'kerbin':{'a':13599840256,'e':0,'r':6e5,'m':5.2915158e22},
		'mun':{'a':12e6,'e':0,'r':2e5,'m':9.7599066e20},
		'minmus':{'a':47e6,'e':0,'r':6e4,'m':2.645758e19},
}