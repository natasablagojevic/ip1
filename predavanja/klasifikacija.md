# Klasifikacija

* Zadatak klasifikacije je zadatak dodeljivanja objekata u jednu ili vise kategorija koje su unapred definisane

* Zadatak klasifikacije je da odredi funkciju koja preslikava svaki atribut u jednu od predefinisanih vrednosti
  * da oslikavamo veze medju ulaznim podacima
  * podatke razdvajamo na **trening** i **test** i oni moraju biti disjunktni
  * trening -> ucenje modela -> modeli -> primena podataka -> zakljucivanje -> test

* **Tehnike klasifikacije**:
  1. Osnovne:
    * drveta odlucivanja
    * pravila
    * neuronske mreze
    * statisticki zasnovane metode
    * masine sa potpornim vektorima
    * odredjivanje najblizeg suseda
    * ...
  2. Metode asambla:
    * pojacavanje
    * pakovanje
    * nasumicna suma
    *  ...

-----
1. **Drveta odlucivanja**
  * postavlja se skup pazljivo odabranih pitanja iz test skupa, svaki put kada dobijemo odgovor da postavimo sledece pitanje koje nas vodi ka novom, i time odredjujemo kojem skupu ce pripadati koji slog
  * listovi - klase, ne-list cvorovi - piranja
  * krecemo od korena, postavljamo pitanja i pratio pratece grane u zavisnosti od odgovora koji se dobio, moze da nas vodi do lista ili ostalih cvorova
  
  >Algoritmi:
  >pohlepni algoritmi - biraju lokalno optimalnonajbolje resenje
  
  * **ID3**
  * **C4.5**
  * **C5.0**
  * **CART (classification and regression tree)**
  * CHAID 
  * Exhaustive CHAID
  * QUEST
  * SLIQ
  * SPRINT
  
  >Opsi model - Hantov algoritam
