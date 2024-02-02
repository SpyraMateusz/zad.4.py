class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania

    @staticmethod
    def znajdz_najstarsza(lista_ksiazek):
        if not lista_ksiazek:
            return None

        najstarsza_ksiazka = min(lista_ksiazek, key=lambda ksiazka: ksiazka.rok_wydania)
        return najstarsza_ksiazka

# Przykład użycia:
ksiazka1 = Ksiazka("Harry Potter", "J.K. Rowling", 1997)
ksiazka2 = Ksiazka("Władca Pierścieni", "J.R.R. Tolkien", 1954)
ksiazka3 = Ksiazka("Złodziejka książek", "Markus Zusak", 2005)

lista_ksiazek = [ksiazka1, ksiazka2, ksiazka3]

najstarsza_ksiazka = Ksiazka.znajdz_najstarsza(lista_ksiazek)

if najstarsza_ksiazka:
    print(f"Najstarsza książka: {najstarsza_ksiazka.tytul} ({najstarsza_ksiazka.rok_wydania})")
else:
    print("Brak książek do sprawdzenia.")