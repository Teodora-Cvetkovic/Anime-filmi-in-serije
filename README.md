# Anime filmi in serije
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


### Analizirala bom:
- Vir:
    - Iz katerega vira je narejeno največ animejev?
    - Kateri vir animeja je najbolj popularen?
    - Ali je popularnost animeja odvisna od vira?
    - Ali je ocena animeja odvisna od vira?
    - Kateri vir animeja ima največjo povprečno oceno?
    - Kateri vir je "najljubši"?
- Čas:
    - Kdaj je izišlo največ animejev?
    - Kdaj so izišli najbolj popularni animeji?
    - V katerem letu je največje povprečno število gledalcev?
    - Katero je "najboljše leto", tj. leto z najvišjo povprečno oceno?
    - Kdaj so izišli najboljši animeji?
    - Ali je popularnost animeja odvisna od tega, ali je leto končanja enako letu izida animeja?
    - Ali je ocena animeja odvisna od tega, ali je leto končanja enako letu izida animeja?
    - Ali je popularnost animeja odvisna od števila epizod?
    - Ali je ocena animeja odvisna od števila epizod?
    - Ali je popularnost animeja odvisna od dolžine epizod?
    - Ali je ocena odvisna od dolžine epizod?
    - V kateri sezoni ima največ popularnih animejev?
    - V kateri sezoni so najboljši animeji?
    - Katera je sezona najbolj popularna?
    - Katera sezona ima najvišjo oceno?
    - Katera je sezona "najljubša"?
- Oznaka:
    - Ali sta popularnost in ocena animeja odvisni od oznake?
    - Katere oznake imajo najbolj popularni animeji?
    - Katere oznake imajo najboljši animeji?
    - Katera oznaka je najbolj popularna?
    - Katera oznaka ima najvišjo povprečno oceno?
    - Katera oznaka je "najljubša"?
    - Ali lahko napovemo oznako animeja iz njegovega naslova in opisa?
- Žanr:
    - Katrih animejev je največ, glede na žanr?
    - Katere žanre imajo najbolj popularni animeji?
    - Katere žanre imajo najboljši animeji?
    - Kateri je žanr najbolj popularen?
    - Kateri žanr ima najvišjo oceno?
    - Kateri je "najljubši žanr"?
    - Ali so ocena in popularnost animeja odvisni od žanra?
    - Ali lahko iz opisa in naslova animeja napovemo njegov žanr?
- Osebe:
    - Kdo je delal na največjem številu animejih?
    - Katera vloga je najpogostejša?
    - Kateri igralec ima največ stranskih in glavnih vlog?
    - Kateri je direktor delal na največjemu številu animejev?
    - Kdo je delal na največjemu številu popularnih animejev?
    - Kdo je delal na največjemu številu najboljših animejev?
    - Kdo ima največje povprečno število členov?
    - Kdo ima najvišjo povprečno oceno?
    - Ali sta popularnost in ocena odvisni od oseb, ki so delale na animeju?
    - Na katerim animejima, glede na oznako, so ljudje najpogostejše delali?
    - V katerem žanru so ljudje najpogostejše delali?
- Studii:
    - Kateri studio je izdelal največ animejev?
    - Kateri studio je najbolj popularen?
    - Kateri studio ima največjo povprečno oceno?
    - Kateri studio je izdelal največ animejev med najbolj popularnimi in najboljšimi animeji?
    - Katere žanre so največ studii delali?
    - Katere animeje, glede na oznako, so delali studii?


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
Datoteka *Anime_serije.ipynb* vsebuje mojo analizo zajetih podatkov. Podatki o animejih so zajeti 13.1.2021 in analizo sem končala 16.1.2021. Če boste sami pobirali podatke, lahko pride do majhnih sprememb v tabelah, ker je mogoče, da se še nek anime konča, lahko še negdo pogleda nek anime, ipn.