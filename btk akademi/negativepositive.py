def negativeorpozitive(number):

    if number == 0:
        print("0 girdiniz")
    elif number > 0:
        print("Pozitif")
    else:
        print("Negatif")


number = int(input("Sayı giriniz: "))
negativeorpozitive(number)