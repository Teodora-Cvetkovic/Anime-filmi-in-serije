# Anime filmi in serije

Analizirala bom podatke o 4290 anime serijah (v nadaljevanju bom pisala *anime* namesto *anime serija*) na spletni strani [MyAnimeList](https://myanimelist.net/). Bom analizirala animeje, kateri so končani. Ker je anime japonska risanka, naslovi so v japonščini ali v angleščini.


### Za vsak anime bom zajela:
- naslov animeja
- datum izida
- datum končanja 
- tip
- koliko anime ima epizod
- opis
- žanre
- oceno
- število členov, kateri so gleali anime
- oznako


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


### Datoteke
Program *MAL_pobiranje.py* bo zajel podatke s strani [MyAnimeList](https://myanimelist.net/), jih obdelal in prečistil, in potem shranil v datoteko *animeji.csv*. V datoteki *animeji.csv* so id animeja, naslov animeja, datum izida in končanja animeja, tip in število epizod animeja, ocena celotnega animeja, opis, oznaka in število gledalcev animeja.