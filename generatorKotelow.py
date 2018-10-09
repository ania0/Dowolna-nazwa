kotely = """=^._.^="""
print(kotely)

owcaUzytkownik = input('Podaj ile kotelow chcesz wygenerowac :) ')

try:
  owcaUzytkownik = int(owcaUzytkownik) 
except ValueError as owcaError:
    owcaUzytkownik = 1
    print("Program potrzebuje liczby a nie ciągu znakow")
    #tu podajecie instrukcje ktore maja sie wykonac jesli uzytkownik zle poda dane czyli bedzie error

print (kotely * owcaUzytkownik)

