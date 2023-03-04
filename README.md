# ip1

---------
# Python
--------------------------
# Funkcije u PANDAS-u
dt = **read_csv(putanja_do_fajla)** <br><br>
dt.**describe()**  :  daje prosecne vrednosti za sve kolone <br><br>
dt.**head()**   :   prvih 5 redova <br><br>
dt.**tail()**   :   poslednjih 5 redova <br><br>
dt.**columns**   : izdvaja nazive kolona <br><br>
dt.**drop(columns=[kol1, kol2, .., kolN])**  :   za izbacivanje kolona <br><br>
**len(**dt**)**   :  velicina baze/tabele <br><br>
dt.**query(uslov)**   :   vraca one kolone za koje vazi zadati uslov (neka vrsta filtriranja) <br><br>
dt.**iloc[a:b, c:d]**   :   tabela koja ima *od a do b redov* i *od c do d kolona* <br><br>
dt.**loc[[redni_brojevi_redova], [nazivi_kolona]]**   : izvdajaju se samo oni redovi ciji su redni brojevi zadati samo sa zadatim kolonama <br><br>
dt.**naziv_kolone.dtype**   :   vraca kog je tipa zadata kolona <br><br>
dt.**dtypes**   : vraca sve kolone kog su tipa<br><br>
dt.**cumsum()** : kumulativni zbir<br><br>
dt.**sample(uslov)**    : ako je baza prevelika, ogranicvamo se da radimo nad samo neki manji podskup od celokupne baze <br><br>
dt.**[kolona].where(uslov)**  :  upituje se skup podataka na osnovu uslova <br><br>
dt.**kolona.unique()**   :  za kategoricke vrednosti, pronalazi samo jedinstvene <br><br>
dt.**kolona.nunique()**   : koliko jedinstvenih vrednosti ima u koloni <br><br>
dt.**kolona.rank()**    :   rang na osnovu zadate kolone <br><br>
dt.**kolona.isin()**    : <br>  <br>
dt.**replace()**  :   <br><br>
dt.**rename(column={staroime: Stari_Naziv, novoime: Novi_Naziv})**  : preimenjuje kolone <br><br>
dt.**kolona.fillna(value, inplace=True)** : zamenjuje NaN vrednosti sa value <br><br>
dt.**count(0)**    : vraca broj datafrejmova, direction = 0 => broj vrednosti u kolonama, 1 => number data in rows <br><br>
dt.**explode()** <br><br>
