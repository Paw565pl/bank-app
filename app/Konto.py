class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_rabatowy=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0

        if len(str(pesel)) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"

        if self.czy_kod_promocyjny_poprawny(kod_rabatowy):
            self.saldo = 50


    def czy_kod_promocyjny_poprawny(self, kod_rabatowy: str) -> bool:
        if kod_rabatowy == None:
            return False
        return len(kod_rabatowy) == 8 and kod_rabatowy[:5] == "PROM_" #TODO: regex