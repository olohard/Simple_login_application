from user import User



if __name__ =="__main__":
    print("Wybierz opcję:")
    print('1.Zaloguj')
    print('2.Zarejestruj')
    x = input("Wybierz opcję")
    if x == 1:
        username = input('Podaj nazwę użytkownika.')
        password = input('Podaj hasło.')
        if u.login(username, password):
            print("Udało ci się zalogować.")
        else:
            print("Niestety nie udało się zalogować.")
    elif x == 2:
        new_username = input('Podaj nowa nazwe uzytkownika:')
        new_password = input('Podaj nowe haslo:')
        new_mail = input('Nowy e-mail:')
        u = User(new_username, new_password, new_mail)  # Tworzymy obiekt klasy User
