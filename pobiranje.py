import orodja
import re
import requests

STEVILO_STRANI = 3
STEVILO_ANIMEJA_NA_STRANI = 30

# url = 'https://anidb.net/anime/?h=1&langid=4&noalias=0&orderby.name=1.1&orderby.ucnt=0.2&page=1&tag.2748=-1&tag.2749=-1&type.movie=1&type.tvseries=1&view=grid'

with open('animeji-stran-1.html') as f:
   vsebina = f.read()

#def nalozi_stran(url):
#    print(f'Nalagam stran {url}...')
#    headers = {
#        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 RuxitSynthetic/1.0 v7069248640 t55095 ath889cb9b1 altpub cvcv=2 smf=0',
#        'Accept-Language': 'de-at;it-it;en-us'
#    }
#    odziv = requests.get(url, headers=headers)
#    return odziv.text

vzorec = (
    r'<a class="name-colored" href="/anime/'
    r'(?P<id>\d+)">'   # ID animeja ima 4 števk
    r'(?P<naslov>.*)'   # naslov animeja
    r'</a>\n.*\n.*?'
    r'(?P<datum_izida>(\d+\.){2}\d+)'   # datum izida animeja
    r'( - )?'
    r'(?P<datum_koncanja>((\d+\.){2}\d+|\?|))'   # datum končanja animeja
    r'(\n.*){3}\n.*?>'
    r'(?P<tip>.*?)'   # ali je anime serija ali film
    r',?'
    r'((?P<epizode>.*?) eps?)?'   # število epizod
    r'\n.*\n.*?'
    r'(?P<ocena>\d\.\d{2})'   # ocena animeja
    r'(.*\n){2}.*?'
    r'(?P<povprecna>\d.\d{2})'   # povprečna ocena animeja po epizodi
    r'.*\n.*?\n.*?<.*?>.*?"tagname">'
    r'(?P<zanri>.*(\n.*){0,11})'   # žanri
    r'</div>\n.*?<div class="desc">'
    r'(?P<opis>.*)'   #opis
)

count = 0
idjevi = []
for zadetek in re.finditer(vzorec, vsebina):
    id_animeja = zadetek.groupdict()['id']
    if id_animeja  not in idjevi:
        idjevi.append(id_animeja)
        print(zadetek.groupdict())
        count += 1
print(count)

najdeni_animeji = 0

#for stran in range(STEVILO_STRANI):
#    start = stran + 1
#    url = f'https://anidb.net/anime/?h=1&langid=4&noalias=0&orderby.name=1.1&orderby.ucnt=0.2&page={stran}&tag.2748=-1&tag.2749=-1&type.movie=1&type.tvseries=1&view=grid'
#    vsebina = nalozi_stran(url)
#    with open(f'popularni-animeji-{start}.html', 'w', encoding='utf-8') as f:
#        f.write(vsebina)
#
#    with open(f'popularni-animeji-{start}.html') as f:
#        vsebina = f.read()
#
#        for zadetek in re.finditer(vzorec, vsebina):
#            print(zadetek.groupdict())
#            najdeni_animeji += 1
#
#print(najdeni_animeji)