class Konto:
    def __init__(self, imie, nazwisko, pesel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0

        if len(str(pesel)) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"
