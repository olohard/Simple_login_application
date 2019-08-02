class User:
    def __init__(self, username, password, email='default', loging_in=0):

        if loging_in == 0:
            self.username = username
            self.password = password
            self.email = email
            self.register()
        elif loging_in == 1:
            self.login(username, password)



    def login(self, username, password):
        if self.check_passphrases(username, password):
            print('Udało sie zalogować')
        else:
            print('Nieudało sie zalogowac')

    def __str__(self):
        return self.username

    def register(self):
        x = open('file.txt', 'w')
        x.write(self.username)
        x.write('\n')
        x.write(self.password)
        x.write('\n')
        x.write(self.email)
        x.close()

    def check_passphrases(self, username, password):
        y = open('file.txt')
        correct_username = y.readline().rstrip()
        correct_password = y.readline().rstrip()

        print(correct_password)
        print(correct_username)
        y.close()
        if correct_username == username:
            if correct_password == password:
                return True
        return False
