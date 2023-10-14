class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_rabatowy=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0

        if len(str(pesel)) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"

        if self.czy_kod_promocyjny_poprawny(
            kod_rabatowy
        ) and self.czy_kwalifikuje_sie_do_promocji(self.pesel):
            self.saldo = 50

    def czy_kod_promocyjny_poprawny(self, kod_rabatowy: str) -> bool:
        if kod_rabatowy == None:
            return False
        return len(kod_rabatowy) == 8 and kod_rabatowy[:5] == "PROM_"  # TODO: regex

    def czy_kwalifikuje_sie_do_promocji(self, pesel: str) -> bool:
        if pesel == "Niepoprawny pesel!":
            return False

        cyfra_roku = int(pesel[0:2])
        cyfra_miesiaca = int(pesel[2:4])

        if cyfra_roku > 60 or cyfra_miesiaca > 12:
            return True
        return False
