from random import randint

#Zad1
A = [1 - x for x in range(1, 11)]
print(A)
B = [4 ** x for x in range(0, 8)]
print(B)
C = [x for x in range(50) if x % 2 == 0]
print(C)

#Zad2
lista1 = []
for i in range(0, 10):
    lista1.append(randint(0, 100))
parzyste = [x for x in lista1 if x % 2 == 0]
print(parzyste)

#Zad3
zakupy = {
    "chleb": "sztuki",
    "woda": "litry",
    "bulki": "sztuki",
    "chrupki": "paczki",
    "jablka": "kg",
    "czekolada": "sztuki"
}

zakupy2 = [key for key in zakupy if zakupy.values() == "sztuki"]
print(zakupy2)
#Nie mam pojęcia dlaczego nic nie wyświetla

#Zad4
def trojkat_prostokatny():
    a = int(input("Podaj bok a trójkąta:"))
    b = int(input("Podaj bok b trójkąta:"))
    c = int(input("Podaj bok c trójkąta:"))
    if a + b > c and a + c > b and b + c > a:
        if (a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2):
            print("Trójkąt jest prostokątny!")
    else:
        print("Trójkąt nie jest prostokątny!")

trojkat_prostokatny()

#Zad5
def pole_trapezu():
    a = 5
    b = 10
    h = 4
    pole = ((a + b) * h)/2
    print("Pole trapezu wynosi:", pole)

pole_trapezu()

#Zad6
def ciag1():
    a = 1
    b = 4
    ile = 10
    ciag = []
    for x in range(0, ile):
        ciag.append(a * (b ** x))
    print(ciag)
ciag1()

#Zad7
