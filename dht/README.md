# Czujnik temperatury i wilgotności powietrza

Najczęstszym wyborem co do tego czujnika jest [Czujnik temperatury i wilgotności DHT11 +50C](https://botland.com.pl/czujniki-multifunkcyjne/9301-czujnik-temperatury-i-wilgotnosci-dht11-50c-5904422372668.html) oczywiście można wybrać opcję z modułem [Czujnik temperatury i wilgotności DHT11 - moduł + przewody](https://botland.com.pl/czujniki-multifunkcyjne/1886-czujnik-temperatury-i-wilgotnosci-dht11-modul-przewody-5903351242448.html) niestety w moim przypadku został wykorzystany model bez modułu.

1. Przekopiuj pliki **dht.py** i **dht11.py**
2. Podepnij odpowiednio przewody do pinów:

- GND -> GND
- VSS -> 3V3
- Data -> GP28

3. Jeśli wszystko dobrze zrobiłeś odpal plik **dht11.py** i sprawdź czy wszystko działa.
