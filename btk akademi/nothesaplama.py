def not_hesaplama(vize_notu,final_notu):
    
    not_hesap = (vize_notu * 0.4 ) + (final_notu * 0.6)
    if not_hesap >= 50:
        print("Başarıyla geçtiniz, geçme notunuz: ",not_hesap)
    else:
        print("Kaldınız")


vize_notu = int(input("vize: "))
final_notu = int(input("final: "))
not_hesaplama(vize_notu,final_notu)




