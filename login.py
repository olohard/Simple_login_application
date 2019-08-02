from user import User



if __name__ =="__main__":
    print("Wybierz opcję:")
    print('1.Zaloguj')
    print('2.Zarejestruj')
    x = int(input("Wybierz opcję"))
    print(x)
    if x == 1:
        username = input('Podaj nazwę użytkownika.')
        password = input('Podaj hasło.')
        i = User(username, password, loging_in=1)
    elif x == 2:
        new_username = input('Podaj nowa nazwe uzytkownika:')
        new_password = input('Podaj nowe haslo:')
        new_mail = input('Nowy e-mail:')
        u = User(new_username, new_password, new_mail)  # Tworzymy obiekt klasy User
