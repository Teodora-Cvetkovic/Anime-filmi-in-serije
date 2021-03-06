import re
import orodja

vzorec_bloka = re.compile(
    r'<td class="borderClass bgColor(0|1)" valign="top">.*?</td></tr>',
    flags=re.DOTALL
)

vzorec = (
    r'<a.*?href=".*?/anime/'
    r'(?P<id>\d+?)/'    # id animeja
    r'(?P<naslov>.*?)"'    # naslov animeja
    r'.*?\n\s*?.*?<div class="pt4">'
    r'(?P<opis>.*?\.\.\.)?'    # opis animeja
    r'.*?\n.+?\n.+?'
    r'\w{2}'
    r'\n.*?\n.*?'
    r'(?P<epizode>(\d+?|-))'    # število epizod
    r'\n.*\n.*?'
    r'(?P<ocena>(\d\.\d{2}|N/A))'    # ocena
    r'\n.*\n.*?'
    r'(?P<zacetek>(\d{2}-\d{2}-\d{2}|\?{0,2}-\?{0,2}-\d{2}|-))'    # mesec, dan in leto začetka prikazovanja
    r'\n.*\n.*?'
    r'(?P<konec>(\d{2}-\d{2}-\d{2}|-|\?{0,2}-\?{0,2}-\d{2}))'    # mesec, dan in leto konca prikazovanja 
    r'\n.*\n.*?'
    r'(?P<stevilo_clenov>\d+?(,\d+?)?(,\d+?)?)'    # število uporabnikov, ko so pogledali anime
    r'\n.*\n\s*?'
    r'(?P<oznaka>(\w.*?|-))'    # uzrast
    r'\n.*?</td>'
)

vzorec_zanra = (
    r'genre/'
    r'(?P<id_zanra>\d+?)/.*?" title="'
    r'(?P<zanr>.*?)">'
)

vzorec_studija = (
    r'Studios:</span>\n.*?<a href="/anime/producer/'
    r'(?P<id_studija>\d+?)/.*?" title="'
    r'(?P<studio>.*?)">'    # studio, ki je naredil anime
)

vzorec_sezone = (
    r'Premiered.*?\n.*?(?P<sezona>(\w+? \d+?|\?))(</a>)?\n'    # sezona, v kateri se je anime začel
)

vzorec_naslova = (
    r'<h1.*?<strong>(?P<naslov>.*?)</strong></h1>'    # naslov brez podčrtaja
)

vzorec_dolzine = (
    r'<span .*?Duration.*\n\s{2}(?P<dolzina>\d+?\s(m|s)|)\w.*?\n'    # dolžina epizode animeja
)

vzorec_vira = (
    r'<span.*?Source.*\n\s{2}(?P<vir>.*?)\n'    # vir, iz katerega je anime narejen
)

vzorec_najljubsega = (
    r'<span.*?Favorites.*?\n\s{2}(?P<najljubsi>\d+?(,\d+?)?)\n'    # število uporabnikov, ki so anime označili kot najljubši
)

vzorec_igralca = (
    r'<small>(?P<vloga>.*?)</small>(\n.*){5}\n.*?'    # ali oseba ima vlogo stranjskega ali glavnega lika
    r'<a href="https://myanimelist.net/people/(?P<id_osebe>\d+?)'
    r'/.*?">(?P<ime_osebe>.*?)</a>.*?\n'    # priimek in ime igralca
)

vzorec_osebja =(
    r'<a href="https://myanimelist.net/people/(?P<id_osebe>\d+?)'
    r'/.*?">(?P<ime_osebe>.*?)</a>.*?\n'    # priimek in ime osebe
    r'.*\n.*?<small>(?P<vloga>.*?)(</small>|,)'    # kaj je oseba delala v proizvodnji animeja
)

def izloci_podatke_animeja(blok):
    anime = re.search(vzorec, blok).groupdict()
    anime['id'] = int(anime['id'])
    anime['stevilo_clenov'] = int(anime['stevilo_clenov'].replace(',', ''))

    if anime['oznaka'] == '-':
        anime['oznaka'] = None

    if anime['opis'] != None:
        anime['opis'] = anime['opis'].replace('&#039;', "'").replace('&quot;', '"')

    if anime['epizode'] == '-':
        anime['epizode'] = None
    else:
        anime['epizode'] = int(anime['epizode'])
    
    if anime['ocena'] == 'N/A':
        anime['ocena'] = None
    else:
        anime['ocena'] = float(anime['ocena'])
    
    if anime['zacetek'] != '-':
        if int(anime['zacetek'][(len(anime['zacetek']) - 2):]) > 21:
            anime['zacetek'] = int('19' + anime['zacetek'][(len(anime['zacetek']) - 2):])
        else:
            anime['zacetek'] = int('20' + anime['zacetek'][(len(anime['zacetek']) - 2):])
    else:
        anime['zacetek'] = None

    if anime['konec'] != '-':
        if int(anime['konec'][(len(anime['konec']) - 2):]) > 21:
            anime['konec'] = int('19' + anime['konec'][(len(anime['konec']) - 2):])
        else:
            anime['konec'] = int('20' + anime['konec'][(len(anime['konec']) - 2):])
    else:
        anime['konec'] = None

    return anime

def animeji_na_strani(stran):
    start = stran * 50
    url= (f'https://myanimelist.net/anime.php?cat=0&q=&type=1&score=0&status=2&p=0&r=0&sm=0&sd=0&sy=0&em=0&ed=0&ey=0&c%5B0%5D=a&c%5B1%5D=b&c%5B2%5D=c&c%5B3%5D=d&c%5B4%5D=e&c%5B5%5D=f&c%5B6%5D=g&gx=1&genre%5B0%5D=9&genre%5B1%5D=12&genre%5B2%5D=26&genre%5B3%5D=28&genre%5B4%5D=33&genre%5B5%5D=34&o=7&w=1&show={start}')
    ime_datoteke = f'zajeti-podatki/popularni_animeji_{stran}'
    orodja.shrani_spletno_stran(url,ime_datoteke)
    vsebina = orodja.vsebina_datoteke(ime_datoteke)
    for blok in vzorec_bloka.finditer(vsebina):
        yield izloci_podatke_animeja(blok.group(0))

def najdi_zanre(datoteka):
    vsebina = orodja.vsebina_datoteke(datoteka)
    zanri = []
    for z in re.finditer(vzorec_zanra, vsebina):
        zanri.append(z.groupdict()['zanr'])
    return zanri

def najdi_studio(datoteka):
    studiji = []
    vsebina = orodja.vsebina_datoteke(datoteka)
    for s in re.finditer(vzorec_studija, vsebina):
        studio = s.groupdict()
        studio['studio'] = studio['studio'].replace('&#039;', "'")
        studiji.append(studio)
    return studiji

def najdi_naslov(datoteka):
    vsebina = orodja.vsebina_datoteke(datoteka)
    for n in re.finditer(vzorec_naslova, vsebina):
        naslov_animeja = n.groupdict()
    return naslov_animeja['naslov']

def najdi_osebe(datoteka):
    osebe = []
    vsebina = orodja.vsebina_datoteke(datoteka)
    for i in re.finditer(vzorec_igralca, vsebina):
        igralec = i.groupdict()
        osebe.append({'id': int(igralec['id_osebe']), 'oseba': igralec['ime_osebe'], 'vloga': igralec['vloga']})
    for o in re.finditer(vzorec_osebja, vsebina):
        osebje = o.groupdict()
        osebe.append({'id': int(osebje['id_osebe']), 'oseba': osebje['ime_osebe'], 'vloga': osebje['vloga']})
    return osebe

def najdi_sezono(datoteka):
    vsebina = orodja.vsebina_datoteke(datoteka)
    for s in re.finditer(vzorec_sezone, vsebina):
        sezona = s.groupdict()
    if sezona['sezona'] == '?':
        return None
    else:
        return sezona['sezona'][:-5]

def najdi_vir(datoteka):
    vsebina = orodja.vsebina_datoteke(datoteka)
    for v in re.finditer(vzorec_vira, vsebina):
        vir = v.groupdict()
    return vir['vir']

def najdi_dolzino(datoteka):
    vsebina = orodja.vsebina_datoteke(datoteka)
    for d in re.finditer(vzorec_dolzine, vsebina):
        dolzina = d.groupdict()
    return dolzina

def najdi_najljubse(datoteka):
    vsebina = orodja.vsebina_datoteke(datoteka)
    for n in re.finditer(vzorec_najljubsega, vsebina):
        najljubsi = n.groupdict()
    return int(najljubsi['najljubsi'].replace(',', ''))



animeji = []
vsi_zanri = []
vsi_studiji = []
studiji_po_animejih = []
osebe = []
vloge = []
id_osebe = []
id_studija = []
for stran in range(87):
    for anime in animeji_na_strani(stran):
        id_animeja = anime['id']
        naslov = anime['naslov']
        url = f'https://myanimelist.net/anime/{id_animeja}/{naslov}'
        ime_datoteke = f'zajeti-podatki/{naslov}'
        orodja.shrani_spletno_stran(url, ime_datoteke)

        zanri_a = najdi_zanre(ime_datoteke)
        for z in zanri_a:
            vsi_zanri.append({'anime': anime['id'], 'zanr': z})

        for studio in najdi_studio(ime_datoteke):
            if studio['id_studija'] not in id_studija:
                vsi_studiji.append(studio)
                id_studija.append(studio['id_studija'])
            studiji_po_animejih.append({'anime': anime['id'], 'studio': studio['id_studija']})

        for oseba in najdi_osebe(ime_datoteke):
            if oseba['id'] not in id_osebe:
                osebe.append({'id': oseba['id'], 'ime': oseba['oseba']})
                id_osebe.append(oseba['id'])
            vloge.append({'anime': id_animeja, 'oseba': oseba['id'], 'vloga': oseba['vloga']}) 

        anime['sezona'] = najdi_sezono(ime_datoteke)
        anime['vir'] = najdi_vir(ime_datoteke)
        anime['dolzina'] = najdi_dolzino(ime_datoteke)['dolzina']

        if anime['dolzina'] == '':
            anime['dolzina'] = None
        else:
            if anime['dolzina'][-1] == 'm':
                anime['dolzina'] = float(anime['dolzina'].replace(' m', ''))
            elif anime['dolzina'][-1] == 's':
                anime['dolzina'] = round(float(anime['dolzina'].replace(' s','')) / 60, 2)

        anime['najljubsi'] = najdi_najljubse(ime_datoteke)
        anime['naslov'] = najdi_naslov(ime_datoteke).replace('&#039;', "'").replace('&quot;', '"')
        animeji.append(anime)



orodja.zapisi_csv(
    animeji,
    ['id', 'naslov','sezona', 'zacetek', 'konec', 'vir', 'epizode','dolzina', 'stevilo_clenov', 'najljubsi', 'ocena', 'opis', 'oznaka'],
    'obdelani-podatki/animeji.csv'
)

orodja.zapisi_csv(
    vsi_zanri, ['anime', 'zanr'], 'obdelani-podatki/zanri.csv'
)

orodja.zapisi_csv(
    vsi_studiji, ['id_studija', 'studio'], 'obdelani-podatki/studiji.csv'
)

orodja.zapisi_csv(
    studiji_po_animejih, ['anime', 'studio'], 'obdelani-podatki/studiji_po_animejih.csv'
)

orodja.zapisi_csv(
    osebe,
    ['id', 'ime'],
    'obdelani-podatki/osebe.csv'
)

orodja.zapisi_csv(
    vloge,
    ['anime', 'oseba', 'vloga'],
    'obdelani-podatki/vloge.csv'
)