# Komentarz
#wyswietlanie tekstu w konsoli:
print("Hello")
print('Hello')
#typ danych -> string
owca = 'owca jest fajna'
#typ danych -> liczby całkowite (init)
owcaJestLiczbaCalkowita = 7
#typ danych ->liczby zmiennoprzecinkowe (float)
owcaJestLiczbaZmiennoPrzecinkowa = 7.5
#tyo danych prawda/falsz (boolean)
owcaPrawda = True
owcaFalsz = False
#szybkie operacje na liczbach
#dzielenie modulo czyli zwracanie reszty z dzielenia
print ( 7%5 ) #wynik to 2
#potegowanie
print (2**5) # 2 do potegi 5
print (2e2) # 2 razy 10 do potegi 2 

#problemy z typami :D
print ("7" + 7) #daje error
print ("7", 7) #daje 77
#funkcja str zamnienia liczbe na napis
print ( '7'+ str(7))
#taki fajny future ale nie wiem jak sie nazywa :D
owcaFajna = 1234
print(f"Owca ma {owcaFajna} lat, stara nie?")