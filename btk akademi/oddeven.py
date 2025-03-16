def odd_even(number):

    if number % 2 == 0:
        print("Sayı çifttir")
    else:
        print("Sayı tektir")


number = int(input("Bir sayı giriniz: "))
odd_even(number)