import re
import orodja
import datetime


vzorec_bloka = re.compile(
    r'<div class=".+?" id=".+?">.*?'
    r'</div>\n\s{3}</div>\n\s{2}</div>',
    flags=re.DOTALL
)

vzorec_animeja = re.compile(
    r'<a class="name-colored" href="/anime/'
    r'(?P<id>\d+)">'   # ID animeja
    r'(?P<naslov>.*)'   # naslov animeja
    r'</a>.*?(?P<datum_izida>(\d+\.){2}\d+)'   # datum izida animeja
    r'( - )?(?P<datum_koncanja>((\d+\.){2}\d+|\?|))'   # datum končanja animeja
    r'.*?"general">(?P<tip>\w{2,5}( \w{6})?)'   # ali je anime serija ali film
    r'(, )?((?P<epizode>.*?) eps?)?'   # število epizod
    r'.*?(?P<ocena>\d.\d{2})'   # ocena animeja
    r'.*?"value">(?P<povprecna>\d.\d{2})'   # povprečna ocena animeja po epizodi
    r'.*?<.*?>.*?("tagname">)?'
    r'(?P<zanri>.*(\n.*){0,11})?'   # žanri
    r'</div>\n.*?<div class="desc">'
    r'(?P<opis>.*)\n',   #opis
    flags=re.DOTALL
)

vzorec_zanra = re.compile(
    r'<span class="tagname">(?P<zanr>.*?)</span>',
    flags=re.DOTALL
)

vzorec_povezave = re.compile(
    r'<a.*?>(.+?)</a>',
    flags=re.DOTALL
)

vzorec_opisa = re.compile(
    r'<div class="desc">(?P<opis>.*?)</div>',
    flags=re.DOTALL
)

vzorec_br = re.compile(
    r'<br /><br />',
    flags=re.DOTALL
)

vzorec_i = re.compile(
    r'<i>(.+?)</i>'
)

vzorec_konca = re.compile(
    r'\n\t\t\t\t</div>\n\t\t\t</div>'
)


def izloci_podatke_animeja(blok):
    anime = vzorec_animeja.search(blok).groupdict()
    anime['id'] = int(anime['id'])
    anime['zanri'] = re.findall(vzorec_zanra, blok)
    anime['datum_izida'] = datetime.date(
        int(anime['datum_izida'][6:]),
        int(anime['datum_izida'][3:5]),
        int(anime['datum_izida'][:2])
    )

    if anime['epizode'] != None:
        anime['epizode'] = int(anime['epizode'])
    else:
        anime['epizode'] = None

    if anime['datum_koncanja'] != '?' and anime['datum_koncanja'] != '':
        anime['datum_koncanja'] = datetime.date(
            int(anime['datum_koncanja'][6:]),
            int(anime['datum_koncanja'][3:5]),
            int(anime['datum_koncanja'][:2])
        )
    else:
        anime['datum_koncanja'] = None

    anime['ocena'] = float(anime['ocena'])
    anime['povprecna'] = float(anime['povprecna'])
    anime['opis'] = vzorec_povezave.sub(r'\1', anime['opis'])
    anime['opis'] = vzorec_br.sub('', anime['opis'])
    anime['opis'] = vzorec_i.sub(r'\1', anime['opis'])
    anime['opis'] = vzorec_konca.sub('', anime['opis'])
    return anime

def animeji_na_strani(stran):
    url = (
        f'https://anidb.net/anime/'
        f'?h=1&langid=4&noalias=0&orderby.name=1.1&orderby.ucnt=0.2&'
        f'page={stran}&tag.2748=-1&tag.2749=-1&type.movie=1&type.tvseries=1&view=grid'
    )
    ime_datoteke = f'zajeti_podatki/popularni_animeji_{stran}'
    orodja.shrani_spletno_stran(url,ime_datoteke)
    vsebina = orodja.vsebina_datoteke(ime_datoteke)
    for blok in vzorec_bloka.finditer(vsebina):
        yield izloci_podatke_animeja(blok.group(0))

def izloci_zanre(animeji):
    zanri = []
    videni_idiji = set()
    for anime in animeji:
        if anime['id'] not in videni_idiji:
            for zanr in anime.pop('zanri'):
                zanri.append({'anime': anime['id'], 'zanr': zanr})
        #zanri.sort(key=lambda anime: anime['id'])

    return zanri

animeji =[]
ids = []
n = 0
for stran in range(51):
    for anime in animeji_na_strani(stran):
        if anime['id'] not in ids:
            animeji.append(anime)
            ids.append(anime['id'])
            n += 1
animeji.sort(key=lambda anime: anime['id'])
zanri = izloci_zanre(animeji)
orodja.zapisi_csv(
    animeji,
    ['id', 'naslov', 'datum_izida', 'datum_koncanja', 'tip', 'epizode', 'ocena', 'povprecna', 'opis'],
    'obdelani-podatki/animeji.csv'
)
orodja.zapisi_csv(zanri, ['anime', 'zanr'], 'obdelani-podatki/zanri.csv')
print(n)


#for anime in animeji_na_strani(1):
#    print(anime['naslov'])