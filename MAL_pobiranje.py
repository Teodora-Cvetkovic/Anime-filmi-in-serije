import re
import orodja
import datetime

vzorec_bloka = re.compile(
    r'<td class="borderClass bgColor(0|1)" valign="top">.*?</td></tr>',
    flags=re.DOTALL
)

vzorec = (
    r'<a.*?href=".*?/anime/'
    r'(?P<id>\d+?)/'    #id animeja
    r'(?P<naslov>.*?)"'    #naslov animeja
    r'.*?\n\s*?.*?<div class="pt4">'
    r'(?P<opis>.*?\.\.\.)?'    #opis animeja (nemaju svi animei opis)
    r'.*?\n.+?\n.+?'
    r'(?P<tip>\w{2})'    #TV serija
    r'\n.*?\n.*?'
    r'(?P<epizode>\d+?)'    #število epizod
    r'\n.*\n.*?'
    r'(?P<ocena>(\d\.\d{2}|N/A))'    #ocena
    r'\n.*\n.*?'
    r'(?P<zacetek>(\d{2}-\d{2}-\d{2}|\?{0,2}-\?{0,2}-\d{2}))'    #mesec, dan, leto začetka prikazovanja (upitnici)
    r'\n.*\n.*?'
    r'(?P<konec>(\d{2}-\d{2}-\d{2}|-|\?{0,2}-\?{0,2}-\d{2}))'    #mesec, dan, leto konca prikazovanja (upitnici)
    r'\n.*\n.*?'
    r'(?P<stevilo_clenov>\d+?(,\d+?)?(,\d+?)?)'
    r'\n.*\n\s*?'
    r'(?P<oznaka>(\w.*?|-))'    #uzrast
    r'\n.*?</td>'
)

vzorec_zanra = (
    r'genre/'
    r'(?P<id_zanra>\d+?)/'
    r'(?P<zanr>.*?)" title'
)

vzorec_studija = (
    r'Studios:</span>\n.*?<a href="/anime/producer/'
    r'(?P<id_studija>\d+?)/'
    r'(?P<studio>.*?)" title'
)

def izloci_podatke_animeja(blok):
    anime = re.search(vzorec, blok).groupdict()
    anime['id'] = int(anime['id'])
    anime['epizode'] = int(anime['epizode'])
    anime['ocena'] = float(anime['ocena'])
    anime['stevilo_clenov'] = int(anime['stevilo_clenov'].replace(',', ''))
    
    if int(anime['zacetek'][6:]) > 20:
        anime['zacetek'] = int('19' + anime['zacetek'][6:])
    else:
        anime['zacetek'] = int('20' + anime['zacetek'][6:])

    if anime['konec'] != '-':
        if int(anime['konec'][6:]) > 20:
            anime['konec'] = int('19' + anime['konec'][6:])
        else:
            anime['konec'] = int('20' + anime['konec'][6:])
    else:
        anime['konec'] = None

    return anime

def animeji_na_strani(stran):
    start = stran * 50
    url= f'https://myanimelist.net/anime.php?cat=0&q=&type=1&score=0&status=2&p=0&r=0&sm=0&sd=0&sy=0&em=0&ed=0&ey=0&c%5B0%5D=a&c%5B1%5D=b&c%5B2%5D=c&c%5B3%5D=d&c%5B4%5D=e&c%5B5%5D=f&c%5B6%5D=g&gx=1&genre%5B0%5D=9&genre%5B1%5D=12&genre%5B2%5D=26&genre%5B3%5D=28&genre%5B4%5D=33&genre%5B5%5D=34&o=7&w=1&show={start}'
    ime_datoteke = f'zajeti_podatki/popularni_animeji_{stran}'
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
    vsebina = orodja.vsebina_datoteke(datoteka)
    for s in re.finditer(vzorec_studija, vsebina):
        studio = s.groupdict()
    return studio

animeji = []
vsi_zanri = []
vsi_studiji = []
for stran in range(3):
    for anime in animeji_na_strani(stran):
        id_animeja = anime['id']
        naslov = anime['naslov']
        url = f'https://myanimelist.net/anime/{id_animeja}/{naslov}'
        ime_datoteke = f'zajeti_podatki/{naslov}'
        orodja.shrani_spletno_stran(url, ime_datoteke)
        zanri_a = najdi_zanre(ime_datoteke)
        for z in zanri_a:
            vsi_zanri.append({'anime': anime['id'], 'zanr': z})
        studio = najdi_studio(ime_datoteke)
        studio['anime'] = anime['id']
        vsi_studiji.append(studio)
        animeji.append(anime)
orodja.zapisi_csv(
    animeji,
    ['id', 'naslov', 'zacetek', 'konec', 'tip', 'epizode', 'stevilo_clenov', 'ocena', 'opis', 'oznaka'],
    'obdelani-podatki/animeji.csv'
)
orodja.zapisi_csv(
    vsi_zanri, ['anime', 'zanr'], 'obdelani-podatki/zanri.csv'
)
orodja.zapisi_csv(
    vsi_studiji, ['id_studija', 'studio', 'anime'], 'obdelani-podatki/studiji.csv'
)