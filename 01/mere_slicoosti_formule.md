# Neke osobine:
1. **Slicnost**:
  * numericka mera koliko su dva objekta slicna
  * sto dva objekta vise lice jedan na drugi, slicnost im je veca
  * cesto se meri na [0, 1]
  * Koristimo:
    >Pronalazak gresaka u podacima i grupa koje su jako slicne
 2. **Razlicitost (rastojanje)**:
  * Numericka mera koliko su dva objekta razlicita
  * Sto dva objekta vise lice jedan na drugi, razlictos im je manja
  * Najmanja razlicitos je cesto 0, dok gornja granica varira
  * Koristimo:
    >Da nadjemo outlajere, izuzetke, granice klastera
---
# **Mere slicnosti - FORMULE**

Funkcije slicnosti/razlicitosti za atribute p i q

| tip | slicnost | razlicitost |
|-----|----------|-------------|
|nominalni| s = p == q ? 1 : 0 | d = p != q ? 1 : 0 |
| redni | s = 1 - (abs(p - q)/(n-1)) | d = abs(p-q)/(n-1) |
| razmerni/intervalni | s = 1 - (d - $min_d$)/($max_d - min_d$)

* Funkcija d je metrika ako je:
  1. pozitivna odredjenost
  2. simetrija
  3. nejednakost trougla

* **Hamingovo rastojanje:** <br>
  * slicnost = 0 => rastojanje se koristi kao mera slicnosti
za dve tacke n-dimenzje <br>
$$\sum_{k=1}^n q_i $$ <br>

$$q_i = 
\begin{cases}
1, & x_i \neq y_i \\
0, & inace
\end{cases}$$

* **Rastojanje Minkovskog:** $L_p$ <br>
$$(\sum_{i=1}^n abs(x_i - y_i)^p)^{1/p} $$ <br>
  * Specijalni slucajevi: <br>
    1. p = 1 -> Menhetn
    2. Euklidsko rastojanje
    3. p -> $\infty$ supremum rastojanje $L_{max}$

* **Mahalanbisovo rastojanje:**
  $$\sqrt{(X-Y)(\sum)^{-1}(X-Y)^T}$$
* **Za binarne atribute:**
  * $X = (x_1, x_2, \dots, x_d)$
  * $Y = (y_1, y_2, \dots, y_d)$
  * $M_{01}$ : broj atrb koji su X = 0 i Y = 1
  * $M_{10}$ : broj atrb koji su X = 1 i Y = 0
  * $M_{00}$ : broj atrb koji su X = 0 i Y = 0
  * $M_{11}$ : broj atrb koji su X = 1 i Y = 1

* **Jednostavno upravljanje koeficijentima:** (SMC) <br>
  $$SMC = \frac{M_{11} + M_{00}}{M_{01} + M_{10} + M_{11} + M_{00}}$$
  
* **Zakardovo upravljanje koeficijentima:** <br>
 $$J = \frac{M_{11}}{M_{01} + M_{10} + M_{11}} $$ 
  
* **Prosireni Zakardovi koeficijenti:** (Tanimoto) <br>
   $$T = \frac{X \cdot Y}{\|\|X\|\|^2 + \|\|Y\|\|^2 - X \cdot Y} $$
  
* **Kosinusna slicnost:**
  * koristi se kod velikog broja parova '00' 
  $$\cos(X,Y) = \frac{X \cdot Y}{\|\|X\|\| \times \|\|Y\|\|} $$  
  
* **Koleracija:**
  $$corr(p,q) = \frac{covariance(p, q)}{\sigma(p) \sigma(q)} $$  
  
  
