# bimg

**Tento koncept je BETA**

Bimg (ByteImage) je obrázkový formát, který se hodí na ukládání velmi malých obrázků ve tvaru čtverce. Každá barva odpovídá jednomu bajtu => obrázek s rozlišením 3x3 pixelů bude mít velikost 9 bajtů (3*3). Formát .bimg (a .bimgc) se kompiluje do .gif formátu, který má podobné vlastnosti. Pro případy, kdy je velikost .gif souboru menší než samotného .bimg souboru, nebo se v obrázku barvy často za sebou opakují, se dá použít .bimgc (ByteImageCompressed) soubor. Tento formát funguje stejně jako .bimg, ale využívá Python kompresní modul zlib.

> velikost souboru [B] = (délka strany obrázku [px])^2

### Výhody:
- Velmi nízká velikost při ukládání velmi malých obrázků
- Automatická komprese => nemusí platit „čím vyšší rozlišení, tím větší velikost oproti ostatním formátům“
### Nevýhody:
- Pouze 256 barev
- Nepodporuje průhlednost
- Obrázky mohou být pouze ve tvaru čtverce
- Dekompilace velkých obrázků do .gif trvá moc dlouho
- .gif je v nějakých případech pořád lepší??

### V plánu:
- Různé (lepší) verze komprese pro .bimgc
- Podpora pro obdélníkové obrázky
- Podpora pro 24-bit barvy
