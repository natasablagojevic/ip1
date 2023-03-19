# Podaci

* Binarizacija - transformacija neprekidne i diskretne atribute u **binarne**
  * neprekidni u kategoricke pa u binarne
* Tekstualni podaci u numericke
* Vremenske u diskretne niske (SAX - simbolicka aproksimacija agregata)
  * delimo u prozorejednakih velicina, i za svaki taj prozor izracunamo prosecnu vrednost atributa za koju je taj prozor odredjen
  * koristimo te srednje vrednosti da bi diskretizovali celokupnu vremensku seriju pomocu tehnike sa intervalima
  * pretpostavlja se da ti prozori imaju normalnu raspodelu
  
* Diskretne niske u numericke
  * broj jednak broju razlicitih simbola
  * svaka serija se konvertuje u multidimenzioni vektor pomocu transformacije talasicima

* Priprema podataka
  * Problemi sa nedostajucim vrednostima
  * Rad sa nekorektnim podacimam
  * Rad sa dupliranim podacima (spajanje vise izvora)
  * Skaliranje i normalizacija (primenjuje na sve vrednosti atributa; moguca promena prirode dokumenata!; norm = vise atributa koji su razlicito skalirani)
  * Redukcija i transformacija podataka (manja kolicina podataka - efikasnija primena algoritma)
    >**Agregacija** : kombinovanje dva ili vise atributa ili objekta u jedan (redukcija podataka; promena skale; 'stabilniji' podaci)
    
    >**Uzimanje uzoraka** : izdvajamo podskupove podataka i nad takvim podacima vrsimo analize
    >porusavamo da napravimo eliminaciju nekih podataka, da smanjimo dimenziju naseg skupa
    >tako sto cemo da napravimo manji skup

    >**Tipovi uzoraka** : 
    > * jednostavno slucajno uzrocenje
    > * uzorcenje sa zamenom (isti objekat moze biti izabran vise puta)
    > * stratifikovano uzorkovanje - uzorkovanje sa raslojavanjem (iz svakog sloja se bira neki deo ili element; biramo jednak broj objekata; veca velicina povecava verovatnocu da ce on biti izabran odnosno reprezentativan)
    
    >Izbor karakteristika (izdvajanje atributa; kostrukcija atributa; ...) 

    >Rotacija podataka 
    
    >Ostale metode dimenzione redukcije:
    > * SVD
    > * LSA 
    > * Talasici
    > * Furijerove transformacije 
    > * Analiza faktora
    > * Multidimenziono skaliranje, brzo preslikavanje, ISOMAP
    > * Spektralna transformacija grafova
    > * ... 
    > 
