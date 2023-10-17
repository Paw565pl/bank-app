from .Konto import Konto

class KontoFirmowe(Konto):
    def __init__(self, company_name, nip):
        self.company_name = company_name

        if len(str(nip)) == 10:
            self.nip = nip
        else:
            self.nip = "Niepoprawny NIP!"