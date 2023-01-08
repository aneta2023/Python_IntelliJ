print("Jestem Kalkulatorem")

# wiek= 30
# print('mam ', wiek , 'lat', 'i lubie:' , 'plywac', 'tanczyc', 'skakac' , sep=(', \n\t'))
#
# dist = 38
# time = 3
# speed = dist/time
# print(speed, 'km/h')

# dist = int(input('Jaki dystans?'))
# time = int(input('ile czasu?'))
# speed_input = dist/time
# print(speed_input, 'km/h')

# lat = int(input('Ile masz lat?'))
# w_miesiacach=lat*12
# print('To bedzie ', w_miesiacach, 'miesiecy', sep='\t')

# biedra=float(input("Jaka jest cena jablek w biedronka?"))
# lidl=float(input("Jaka jest cena jablek w lidl?"))
# zaba=float(input("Jaka jest cena jablek w zabka?"))
# najtansze=min(biedra,lidl,zaba)
# print("Najtansze jablka kosztuja: ", najtansze)

# wartosc_lokaty = 123.45678999
# print(f'Wartosc lokaty zakoraglona: {wartosc_lokaty:.2f}')

# twoje_imie = input('Jak masz na imie?')
# print(f"Twoje imie zawiera {len(twoje_imie)} literek")
#
# miasto = input("Gdzie mieszkasz?")
# print (f'Jak milo ze mieszkasz w {miasto.title()}')

# favourite_sports = [
#     'ski', 'read', 'gardening', 'yoga', 'painting'
# ]
# print("pierwszy " + favourite_sports[0])
# print(f"pierwszy {favourite_sports[0]}")
# print(f"Dlugosc: {len(favourite_sports)}")
# print(f"Ostatni: {favourite_sports[-1]}")

# potrawy_uzytkownika = input("Podaj 3 ulubione potrawy")
# lista_potraw = potrawy_uzytkownika.split(',')
# print(f"Lista potraw {lista_potraw}")

# slownik = {
#     'matematyka': 5,
#     'polski': 2,
#     'biologia': 3,
#     'historia': 4
# }
# print(slownik)

# print(type(None))
# print(type(3))

# jablko = 13.6
# marchew = 14.8
# cebula = 33.56
#
# print(f'Cena jablek jest mniejsza niz marchewki {jablko<marchew}')
# wynik = cebula>marchew
# print(type(wynik))

# Zapytaj użytkownika o jego oceny końcowe z kilku przedmiotów (matematyka, fizyka, itd.).
#
# Następnie, przeanalizuj je i wypisz informację czy zdał/zdała do kolejnej klasy.
#
# Załóż, że zdać można wtedy jeżeli nie ma się żadnej jedynki albo jeżeli ma się jedną jedynkę, ale średnia ze wszystkich ocen jest wyższa niż 3.5.
# lista_ocen=[]
# ocena_matma = int(input("Jaka jest ocena matma?"))
# lista_ocen.append(ocena_matma)
# ocena_biola = int(input("Jaka jest ocena biola?"))
# lista_ocen.append(ocena_biola)
# ocena_hista = int(input("Jaka jest ocena hista?"))
# lista_ocen.append(ocena_hista)
# print(f"Lista ocen:  {lista_ocen}")
# srednia = float(ocena_matma+ocena_biola+ocena_hista)/3
#
# if ocena_matma > 2:
#         print(f'Zdales z matmy bo masz na koniec {ocena_matma}')
# else:
#     print(f'Nie Zdales z matmy bo masz na koniec {ocena_matma<2},wiec jestes osiol')
#
# print(f'Twoja srednia ocen to {srednia}')

# value = True
#
# if value == True:
#     print("jest true ")
#
# if value is True:
#     print("jest  IS true ")
#
#     value = 12
#
# if value == True:
#     print("jest true ")
#
# if value is True:
#     print("jest  IS true ")

# Poproś użytkownika o podanie ulubionych dań, rozdzielając każde z nich przecinkiem.
#
# Następnie wypisz każde z nich wraz z informacją, które miejsce zajmuje na jej/jego liście.

# favourite_dish = input("Podaj ulubione danie, rozdzielajac przecinkiem")
# favourite_dish = favourite_dish.split(',')
#
# print(favourite_dish)
#
# letter_index = 0
# while letter_index <  len(favourite_dish):
#     # print(favourite_dish[letter_index])
#     print(f"[{letter_index}] --> {favourite_dish[letter_index]}")
#     letter_index += 1
