# ===== 1. VARIABEL DAN TIPE DATA =====
nama = "Windi Sri Rahayu"          # string
umur = 29               # integer
tinggi = 1.6           # float
is_mahasiswa = True     # boolean

print(nama, umur, tinggi, is_mahasiswa)


# ===== 2. INPUT DARI USER =====
nama_input = input("Masukkan nama Anda: ")
print("Halo, " + nama_input)


# ===== 3. OPERATOR =====
a = 10
b = 3
print(a + b)   # penjumlahan
print(a - b)   # pengurangan
print(a * b)   # perkalian
print(a / b)   # pembagian (hasil float)
print(a // b)  # pembagian bulat
print(a % b)   # sisa bagi (modulus)
print(a ** b)  # pangkat


# ===== 4. PERCABANGAN (IF-ELSE) =====
nilai = 80
if nilai >= 90:
    print("Grade A")
elif nilai >= 75:
    print("Grade B")
else:
    print("Grade C")


# ===== 5. PERULANGAN (LOOP) =====
# for loop
for i in range(5):
    print("Perulangan ke-", i)

# while loop
angka = 0
while angka < 3:
    print("Angka:", angka)
    angka += 1


# ===== 6. LIST (ARRAY) =====
buah = ["apel", "jeruk", "mangga"]
buah.append("pisang")   # tambah item
print(buah)
print(buah[0])           # akses item pertama

for b in buah:
    print(b)


# ===== 7. DICTIONARY =====
mahasiswa = {
    "nama": "Windi Sri Rahayu",
    "umur": 29,
    "jurusan": "RPL"
}
print(mahasiswa["nama"])


# ===== 8. FUNGSI =====
def sapa(nama):
    return f"Halo, {nama}!"

print(sapa("Ani"))


def tambah(a, b):
    return a + b

hasil = tambah(5, 3)
print("Hasil penjumlahan:", hasil)


# ===== 9. CLASS (OOP DASAR) =====
class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def perkenalan(self):
        return f"Nama saya {self.nama}, umur {self.umur} tahun"

orang1 = Orang("Hafshah", 22)
print(orang1.perkenalan())