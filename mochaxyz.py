import mochaastro

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
'bee',
'hi',
'info',
'link',
'moquote',
'prequel',
'spidey',
'tng'
]

special = {
'alexa':'do i look like a slave to you?',
'ban':'u can\'t make me!!!',
'cobot':'...not happening.',
'daily':'the hell you think i\'m gonna pay you for?',
'egu':'https://www.youtube.com/watch?v=3-rfBsWmo0M',
'hey google':'hey yourself faggot',
'kill':'nuuuu!~',
'legs':'https://www.youtube.com/watch?v=ZFUd-RbAr-s',
'level':'Your current level is -89237522573987, lol kys n00b',
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
'tng':'https://www.youtube.com/watch?v=kRXry95Q6e0',
'up':'five more minutes sky daddy',
'vc':'\U0001F1FB \U0001F1E8',
'you\'re matched':'say hello! ;)',
'yuri':'https://yuri.dance/'
}

specialer = {
'<@!431483983088451584>':'whazaa??~ ;3',
'maltese falcon':'It\'s the stuff that dreams are made of.',
'mobot':'das meee!~~ :3',
'mobutt':'\u0ca0_\u0ca0',
'moobot':'🐮',
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
'ld':384402000,
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
}
quit = ('exit','quit')

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