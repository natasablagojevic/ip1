# Normalizacja
- cilj je transformacija atributa da budu na slicnim skalama

* **MinMax scaler** <br>
  * $$[min, max] -> [0, 1] $$
  * koristi se kada:
  >Ako priblizno znamo gornje i donje ogranicenje.  
    + ako ne znamo, ne bismo znali da izvedemo formulu <br><br>
  >Ako podaci sadrze malo ili ne sadrze autlajere. 
    + ne bismo mogli da nadjemo MIN i MAX, jer bi podaci bili dosta grupisaniji u jednom delu i ne bismo mogli da nadjemo min i max zapravo <br><br>
  >Ako su podaci priblizno uniformno distribuirani na rasponu. 
    + ako imamo velike gepove, onda kada ih budemo preslikali, tamo gde je veca gustina ce se podaci sabiti i ne bismo mogli da procenimo nista<br><br>

$$x_{novo} = \frac{x - min}{max - min} $$

* **Odescanje**
  >Vrsi se pre ili posle normalizacije. Bitan nam je raspon od a do b, i odsecanje vrsimo $\leq a \Rightarrow a$ i $\geq b \Rightarrow b$. (Svi koji imaju platu vecu od 100_000 kao 100_000); ako imamo ekstremne autlajere kojih zelimo da se otarasimo

$$clipping(x, min, max) = 
\begin{cases}
min,  & x < min \\
max, & x > max \\
\frac{x - min}{max - min}, & inace
\end{cases}$$

* **Logaritamsko slakiranje**
  >Koristi se za modeliranje drustva. Menjamo raspodelu tako da ona bude blaza i zato koristimo logaritam. Vrsimo lograitamsko skaliranje <br>
  
  $$x_{novo} = \log(x) $$
  
* **Z-score** (standardizacija)
  >Imamo neku raspodelu, koliko standardnih devijacija odstupa. Dobro je ako imamo autlajere, jer ne bi trebalo da ih ima mnogo i nece uticati mnogo na standardnu devijaciju i ocekivanu srednju vrednost. Najbolje je koristiti standardizaciju jer tu ne mozemo da pogresimo

  $$x_{novo} = \frac{x - \mu}{\sigma} $$
