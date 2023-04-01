import cv2

cap = cv2.VideoCapture(0)

licznik = 0

# odczytanie wartości licznika z pliku, jeśli plik istnieje
try:

    if os.path.exists('licznik.txt') and os.path.getsize('licznik.txt') > 0:
        with open('licznik.txt', 'r') as f:
        licznik = int(f.readline())

except FileNotFoundError:
    pass

while True:
    # przechwytywanie klatki z kamery
    ret, frame = cap.read()

    # wyswietlanie klatki
    cv2.imshow('frame', frame)

    # nacisniecie s zapisuje zdjecie
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('img{}.png'.format(licznik), frame)
        licznik += 1

        # zapisanie wartości licznika do pliku
        with open('licznik.txt', 'w') as f:
            f.write(str(licznik))

    # nacisniecie q konczy wyswietlanie i zamyka program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# zwolnienie kamery i zamkniecie okna
cap.release()
cv2.destroyAllWindows()
