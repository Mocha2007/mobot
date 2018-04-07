import mochaastro

coffees = {
'':'coffee',
'americano':'espresso\nhot water',
'cappuccino':'double espresso\nsteamed milk foam',
'espresso':'coffee brewed by expressing or forcing out a small amount of nearly boiling water under pressure through finely ground coffee beans',
'flat white':'microfoam poured into a:\nsingle or double shot of espresso',
'grande':'16 oz cup',
'hot milk':'milk\nheat',
'latte':'espresso\nhot milk',
'long black':'A long black is made by pouring a double-shot of espresso or ristretto over hot water.',
'macchiato':'espresso\nhot milk',
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