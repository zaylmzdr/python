import re 

def password_mail(mail_address, password):
    # Mailin '@gmail.com' ile bitmesi gerekiyor
    mail_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@gmail\.com$')

    # Şifre en az 8 karakter olmalı (Eğer ek şartlar isteniyorsa buraya eklenebilir)
    password_regex = re.compile(r'^.{8,}$')

    result_mail = bool(mail_regex.fullmatch(mail_address))
    result_password = bool(password_regex.fullmatch(password))

    if result_password and result_mail:
        print("Başarıyla şifre ve mail oluşturdunuz!")
    elif result_password and not result_mail:
        print("Maili yanlış oluşturdunuz")
    elif not result_password and result_mail:
        print("Şifreyi yanlış oluşturdunuz")
    else:
        print("Mail ve şifreyi yanlış oluşturdunuz")

mail = input("Mail: ")
password = input("Şifre: ")
password_mail(mail, password)
