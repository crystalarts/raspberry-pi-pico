# Wyświetlacz LCD

Aby uruchomić plik **lcd_display.py** musisz posiadać jakikolwiek wyświetlacz LCD w moim przypadku został wykorzystany [Wyświetlacz LCD 2x16 znaków niebieski + konwerter I2C LCM1602](https://botland.com.pl/wyswietlacze-alfanumeryczne-i-graficzne/2351-wyswietlacz-lcd-2x16-znakow-niebieski-konwerter-i2c-lcm1602-5904422309244.html)

1. Przekopiuj pliki **lcd_display.py**, **[lcd_api.py**, **pico_i2c_lcd.py**
2. Podepnij odpowiednio złącza do pinów:

- GND -> GND
- VSS -> V5
- SCL -> Pin 1
- SDA -> Pin 0

3. Sprawdź czy wyświetlacz się uruchomił.
4. Odpal plik **lcd_display.py**
5. Jeśli ekran nic nie wyświetla a uruchamia się ponownie sprawdź czy masz ustawiony potencjometr
