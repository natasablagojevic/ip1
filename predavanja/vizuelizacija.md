# Vizuelizacija rezultata

* **Vizuelizacija** je konverzija podataka u vizuelni ili tabelarni format i pokusavamo da zadrzimo bitne karakteristike

* **Izbor vrste**:
  * zavisi od podataka 
  * mali broj dimenzija objekata moze da se preslika u 2D ili 3D reprezentaciju
  * kada imamo veliki broja atributa tada treba da izaberemo ih u parove ili podskup 
  * preslikavanje atributa i njihovih veza u skup atributa u graficke elemente: tacke, linije, bolici, boje, ..
  * odnosi medju objektima se predtstavljaju grafovskim prikazom

* **Tehnike vizuelizacije**:
  * Uredjenost - moze da utice na razumevanje
  * 1 *Histogram* - sa malim brojem atributa
  * 2 *Kucice* (box-plot)  - podela prema percentilima
  * 3 *Seme sa rasprsenim elementima*
  * 4 *Seme sa konturama* - kada su nerekidni atributi mere u prostornoj osnovi; dele ravan u regione sa slicnim vrednostima
  * 5 *Seme sa matricama* (toplotne mape) - preuredimo objekte tako da objekti koji pripadaju jednoj klasi budu zajedno
  * 6 *Paralelne koordinate* - svaki atribut ima svoju koordinatnu osu i njegova vrednost se predstavlja tackom na koordinatnoj osi i te tacke spajamo linijama, koje odgovaraju odgovarajucoj koordinatnoj osi
    >Otkrivanje sablona zavisi od redosleda u kome spajamo atribute, tj. koordinate
    >ako se previse seku slika je haoticna i nista ne razumemo
    >cilj je da nekako permutujemo da bismo dobili nesto razumljivije
  
  * 7 *Crtanje zvezda* -slican kao kod paralelnih koordinata, s tim da se ose granaju iz centra
  * 8 *Chernoff-ova lica* - da se vrednosti preslikavaju u neke graficke elemente koji su nam poznati kao sto su lica, da svaki atribut bude predstavljen delom lica
  * 9 *Dijagram Voronoi-a* - za odredjeni skup tacaka dijagrama podela se pravi u regione u kome su tacke unutar bliza tom cvoru nego nekom drugom
  * 10 *Slike i tabele* 
  * 11 *Corovi u mrezi* 
  * 12 *Mrreza povezanosti* 
  * 13 *Kombinacija slika* 
  * 14 *Animacije* 

