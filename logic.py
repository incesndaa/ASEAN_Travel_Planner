class MataUang:
    def __init__(self, mataUangAsal, mataUangTujuan, jumlah):
        self.mataUangAsal = mataUangAsal
        self.mataUangTujuan = mataUangTujuan
        self.jumlah = jumlah
        self.kurs = {
            "IDR": {"MYR": 0.0002785, "SGD": 0.00008426, "THB": 0.002126, "PHP": 13.12, "BND": 0.00008426, "VND": 1.588, "KHR": 0.2514, "LAK": 1.369, "MMK": 0.1314},
            "MYR": {"IDR": 3592, "SGD": 0.3026, "THB": 7.638, "PHP": 4.44, "BND": 0.3026, "VND": 5705, "KHR": 903.0, "LAK": 4917, "MMK": 471.9},
            "SGD": {"IDR": 11860, "MYR": 3.304, "THB": 25.25, "PHP": 43.36, "BND": 1, "VND": 18840, "KHR": 2982, "LAK": 16240, "MMK": 1559.23},
            "THB": {"IDR": 469.7, "MYR": 0.1308, "SGD": 0.03961, "PHP": 1.718, "BND": 0.03961, "VND": 746.1, "KHR": 118.1, "LAK": 643.0, "MMK": 61.74},
            "PHP": {"IDR": 273.7, "MYR": 0.07618, "SGD": 0.02306, "THB": 0.5823, "BND": 0.02306, "VND": 434.5, "KHR": 68.76, "LAK": 374.4, "MMK": 35.93},
            "BND": {"IDR": 11860, "MYR": 3.303, "SGD": 1.000, "THB": 25.25, "PHP": 43.36, "VND": 18840, "KHR": 2981, "LAK": 16230, "MMK": 1558.48},
            "VND": {"IDR": 0.6296, "MYR": 0.0001754, "SGD": 0.00005308, "THB": 0.001340, "PHP": 0.002302, "BND": 0.00005307, "KHR": 0.1583, "LAK": 0.8618, "MMK": 0.08274},
            "KHR": {"IDR": 3.978, "MYR": 0.001108, "SGD": 0.0003353, "THB": 0.008462, "PHP": 0.01455, "BND": 0.0003353, "VND": 6.318, "LAK": 5.445, "MMK": 0.5226},
            "LAK": {"IDR": 0.7306, "MYR": 0.0002035, "SGD": 0.00006158, "THB": 0.001554, "PHP": 0.002671, "BND": 0.00006156, "VND": 1.160, "KHR": 0.1837, "MMK": 0.09598},
            "MMK": {"IDR": 7.614, "MYR": 0.002120, "SGD": 0.0006419, "THB": 0.01621, "PHP": 0.02783, "BND": 0.0006419, "VND": 12.09, "KHR": 1.913, "LAK" : 10.42}
        }

    def konversi(self):
        try:
            return self.jumlah * self.kurs[self.mataUangAsal][self.mataUangTujuan]
        except KeyError:
            return "Konversi tidak tersedia untuk mata uang yang dipilih."
        
class AnggaranPerjalanan:
    def __init__(self, biayaTransportasi, biayaAkomodasi, biayaMakanan, biayaTakTerduga):
        self.biayaTransportasi = biayaTransportasi
        self.biayaAkomodasi = biayaAkomodasi
        self.biayaMakanan = biayaMakanan
        self.biayaTakTerduga = biayaTakTerduga

    def hitungAnggaran(self):
        totalBiaya = self.biayaTransportasi + self.biayaAkomodasi + self.biayaMakanan + self.biayaTakTerduga
        return totalBiaya
    
class Tabungan:
    def __init__(self, anggaranPerjalanan, durasiTabungan, jumlahYangSudahDitabung):
        self.anggaranPerjalanan = anggaranPerjalanan
        self.durasiTabungan = durasiTabungan
        self.jumlahYangSudahDitabung = jumlahYangSudahDitabung
    
    def hitungTabungan(self):
        sisaAnggaran = self.anggaranPerjalanan - self.jumlahYangSudahDitabung
        if sisaAnggaran <= 0:
            return 0 
        else:
            return sisaAnggaran / self.durasiTabungan