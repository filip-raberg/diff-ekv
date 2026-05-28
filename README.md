## Förklaring bakom området
Vi har tidigare fokuserat på att lösa differentialekvationer analytiskt, d.v.s med papper och penna för att hitta en exakt matematisk formel.
I verkligheten är de system vi vill undersöka som t.ex väderprognoser, rymdfärder eller bilars stötdämpning oftast så komplexa att det är omöjligt att hitta en exakt formel. Det är då programmering blir nödvändigt.
Genom att använda programmering kan man istället lösa ekvationerna numeriskt. Detta betyder att datorn inte försöker tänka ut en komplex formel, utan istället använder avancerade beräkningar för att simulera förloppet steg för steg.
Koden utgår från ett startvärde, t.ex 2 meter upp, hastighet 0. Den beräknar sedan krafterna och accelerationen just i det momentet och räknar sedan ut vart bilen är precis efter, osv. Denna process upprepas tusentals gånger för att få ett fullt och precist resultat.
Vi får då en exakt approximation visuellt av verkligheten. Ett sånt här program låter t.ex ingenjörer testa och bygga säkra system digitalt innan de faktiskt gör en fysisk prototyp.

## Formler
Den generella differnetialekvationen (andra ordningen)
$$m \frac{d^2x}{dt^2} + c \frac{dx}{dt} + kx = 0$$

Första ordningen i koden
$$\frac{dx}{dt} = v$$
$$\frac{dv}{dt} = \frac{-cv - kx}{m}$$

Startvilkoren
$$x(0) = 2.0 \quad \text{och} \quad v(0) = 0.0$$

## Förklaring av variabler
m = Bilens vikt i kg. En högre massa gör att grafen svänger långsammare (tröghet).
k = Styvhet av fjädern. Ju högre värde desto mer styv är fjädern och vill trycka tillbaks bilen till original-läget.
c = Bestämmer hur mycket stötdämparen bromsar rörelsen. Lågt värde innebär att bilen kommer att gunga mer medans ett högre värde stannar gungandet snabbt.
t = Aktuell tidpunkt
x = Hur långt från ursprung som som bilen befinner sig just nu.
v = Hur snabbt bilen rör sig upp och ner just nu.
dxdt = Förändring av position över tid. Per definition samma som v.
dvdt = Bilens acceleration (förändring av hastighet över tid). Beräknas med newtons andra lag.
y0 = Startvilkor vid t = 0.
t_span = Grafen beräknas från t = 0 till t = 5 (sekunder).
t_eval = Antal punkter som som beräknas.
sol = Lösningen av hela funktionen. Innehåller all data för att rita grafen.
    sol.t = Alla tidspunkter.
    sol.y = Alla positionsvärden för y-axeln.

## Anvädning av AI
Jag har använt AI för delar av min kod som t.ex användning av olika bilbiotek jag inte har tidigare erfarenhet av och uppritningen av funktionerna. Detta lät mig fokusera mer på den matematiska delen av projektet.