class Mahsulot:
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx

    def yetkazib_berish_narxi(self, shahar):
        return 15000 if shahar == "Toshkent" else 25000

    def chegirma_qollash(self, foydalanuvchi):
        return self.narx

    def kafolat_muddati(self):
        return None


class Elektronika(Mahsulot):
    def __init__(self, nom, narx, kafolat_oy):
        super().__init__(nom, narx)
        self.kafolat_oy = kafolat_oy

    def chegirma_qollash(self, foydalanuvchi):
        return self.narx * 0.9  # 10% chegirma

    def kafolat_muddati(self):
        return self.kafolat_oy


class Kiyim(Mahsulot):
    def chegirma_qollash(self, foydalanuvchi):
        return self.narx * 0.95  # 5% chegirma


class Kitob(Mahsulot):
    def chegirma_qollash(self, foydalanuvchi):
        return self.narx  # kitobda chegirma yo‘q


# --- Savat ---
savat = [
    Elektronika("Telefon", 3_000_000, 12),
    Kiyim("Kurtka", 400_000),
    Kitob("Python darsi", 100_000)
]

umumiy = sum(item.chegirma_qollash("ali") + item.yetkazib_berish_narxi("Toshkent") for item in savat)

print("Savat umumiy narxi:", umumiy)
print("Telefon kafolati:", savat[0].kafolat_muddati())
