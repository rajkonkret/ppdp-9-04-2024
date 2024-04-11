# napisac funkcje kantor
# ma posiadac dwie funkcje wewnętrzne
# w zaleznosci od parametru ma zwrócic jedna z nich usd, eur
# możliwośc przekazania dowolnej kwoty
# uwzględnic parametry o wartościach opcjonalnych

def kantor(waluta):
    print("Uruchomienie kantoru")

    def eur(kwota=0):
        print("Wymieniam euro", kwota * 4.26)

    def usd(kwota=0):
        print("Wymieniam dolary", kwota * 3.97)

    if waluta == 'eur':
        return eur
    else:
        return usd


kantor_usd = kantor("usd")
kantor_usd()
kantor_eur = kantor("eur")
kantor_eur()

kantor_usd(1000)
kantor_eur(5000)
# Uruchomienie kantoru
# Wymieniam dolary 0.0
# Uruchomienie kantoru
# Wymieniam euro 0.0
# Wymieniam dolary 3970.0
# Wymieniam euro 21300.0
