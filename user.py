class User:
    def __init__(self, username, password, email, loging_in=0):

        if loging_in == 0:
            self.username = username
            self.password = password
            self.email = email
            self.register()
        elif loging_in == 1:



    def login(self, username, password):
        if self.check_passphrases():
            return True
        return False

    def __str__(self):
        return self.username

    def register(self):
        x = open('file.txt', 'w')
        x.write(self.username)
        x.write(self.password)
        x.write(self.email)
        x.close()

    def check_passphrases(self, username, password):
        y = open('file.txt')
        correct_username = y.readline()
        correct_password = y.readline()