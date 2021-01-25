# Anime serije
*Projektna naloga pri predmetu **Programiranje 1** na Fakulteti za matematiko in fiziko*

Analizirala bom podatke o 4298 anime serijah (v nadaljevanju bom pisala *anime* namesto *anime serija*) na spletni strani [MyAnimeList](https://myanimelist.net/). Bom analizirala animeje, ki so končani. Ker je anime japonska risanka, naslovi bodo v japonščini ali v angleščini.


### Za vsak anime bom zajela:
- naslov animeja
- sezono izida, datum izida in datum končanja 
- število epizod in dolžino animeja
- opis in žanre
- oceno animeja
- število členov, kateri so gleali anime
- število členov, ki so označili anime kot najljubši
- oznako in vir animeja
- osebe, ki so delale na animejima, in njihove vloge
- studie, ki so naredili animeje


### Delovne hipoteze:
- Vir:
    - Največ animejev je narejeno iz mang
    - Največjo povprečno oceno in število členov, ki so pogledali anime, imajo animeji, ki so narejeni iz mang
    - Največ najboljših in najbolj popularnih animejev je narejeno iz mang
- Čas:
    - Največ animejev je izišlo v 21. stoletju in v 2010-ih
    - Kdaj so izišli najbolj popularni animeji?
    - V katerem letu je največje povprečno število gledalcev?
    - Katero je "najboljše leto", tj. leto z najvišjo povprečno oceno?
    - Največ animejev se je končalo v 21. stoletju
    - Več je animejev, ki imajo isto leto začetka in končanja
    - Popularnost in ocena animeja sta odvisni od tega, ali je leto končanja enako letu izida animeja
    - Popularnost in ocena animeja sta odvisni od števila epizod
    - Popularnost in ocena animeja sta odvisni od dolžine epizod
    - Največ animejev ima 12 epizod
    - Epizode največjega števila animejev trajajo 24 minut
    - Pomladi se je začelo največje število animejev
    - Sezona, ki je najbolj popularna, je poletje
    - Sezona z največjo oceno je pomlad
- Oznaka:
    - Popularnost in ocena animeja sta odvisni od oznake animeja
    - Največ animejev ima oznako PG-13
    - Oznaka z največkim številom členov je PG-13
    - Oznaka z najvišjo povprečno oceno je PG-13
    - Lahko napovemo oznako animeja iz naslova in opisa
- Žanr:
    - Največ animejev ima žanr akcija
    - Žanr, z največjim povprečnim številom gledalcev, je komedija
    - Najvišjo povprečno oceno ima žanr akcija
    - Ocena in popularnost animeja sta odvisni od žanra
    - Iz opisa in naslova animeja lahko napovemo njegov žanr
- Osebe:
    - Kdo je delal na največjem številu animejev?
    - Največ je stranskih likov
    - Kateri igralec ima največ stranskih in glavnih vlog?
    - Kateri je direktor delal na največjemu številu animejev?
    - Kdo je delal na največjemu številu popularnih animejev?
    - Kdo je delal na največjemu številu najboljših animejev?
    - Kdo ima največje povprečno število členov?
    - Kdo ima najvišjo povprečno oceno?
    - Popularnost in ocena nista odvisni od osebe, ki je delala na njem
    - Ljudje najpogostejše delajo na animejih z oznako PG-13
    - Ljudje najpogostejše delajo v komedijah
- Studii:
    - Kateri studio je izdelal največ animejev?
    - Kateri studio je najbolj popularen?
    - Kateri studio ima največjo povprečno oceno?
    - Kateri studio je izdelal največ animejev med najbolj popularnimi in najboljšimi animeji?
    - Popularnost in ocena sta odvisna od studia, ki je izdelal anime
    - Studii največ delajo akcijske animeje
    - Studii največ delajo animeje z oznako PG-13


### Datoteke
Program *MAL_pobiranje.py* pobira podatke s strani [MyAnimeList](https://myanimelist.net/), jih obdela in prečisti, in potem shrani.<br>
Datoteka *orodja.py* je pomožna datoteka, katera vsebuje fukcije z pobiranje podatkov.<br>
Zajeti podatki so v mapi *zajeti-podatki*. Tukaj se nahajajo vse html datoteke, katere program mora obdelati.<br>
Ko program obdela podatke, jih shrani v mapo *obdelani-podatki*. Tukaj so tabele napisane v csv datotekami. V datoteki *animeji.csv* so podatki o animejima:
- id animeja,
- naslov animeja,
- sezona začetka animeja,
- datumi začetka in končanja animeja,
- število in dolžina epizod,
- vir iz katerega je narejen anime,
- število uporabnikov, ki so pogledali anime,
- število uporabnikov, ki so označili anime kot najljubši,
- oceno animeja,
- opis animeja
- oznako animeja.

V datoteki *osebe.csv* so id in ime oseb, ki so delale na animejima. V datoteki *studiji_po_animejih.csv* so idijevi studia in animeja. Tista datoteka povezuje datoteki *animeji.csv* in *studiji.csv*. V datoteki *studiji.csv* so idijevi studiev in nazivi studiev. V datoteki *vloge.csv* so povezane osebe in animeji prek idijeva in je napisana vloga oseb v animeju. Na koncu, v datoteki *zanri.csv* so napisani žanri animejev.<br>
Datoteka *Anime_serije.ipynb* vsebuje mojo analizo zajetih podatkov. Podatki o animejih so zajeti 13.1.2021 in analizo sem končala 16.1.2021. Če boste sami pobirali podatke, lahko pride do majhnih sprememb v tabelah, ker je mogoče, da se še nek anime konča, lahko še nekdo pogleda nek anime, ipn.