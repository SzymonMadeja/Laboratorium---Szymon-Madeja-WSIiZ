droga = float(input("Podaj przebyty dystans: ")) # Używamy funkcji float() aby móc operować na podanycb liczbach (dodawać/mnożyć/dzielić) oraz aby mogły być one zmiennoprzecinkowe
srednie_spalanie = float(input("Podaj średnie spalanie samochodu (w litrach na 100km): ")) # Używamy funkcji float() aby móc operować na podanycb liczbach (dodawać/mnożyć/dzielić) oraz aby mogły być one zmiennoprzecinkowe
cena_paliwa = 6.5 # Przypisanie do zmiennej "cena_paliwa" liczby "6.5"
spalanie = srednie_spalanie * (droga / 100) # Obliczenie spalania samochodu
koszt_podrozy = spalanie * cena_paliwa # Obliczenie kosztu podróży

print("Koszt podróży wynosi:",koszt_podrozy) # Wypisanie tekstu z użyciem zmiennych