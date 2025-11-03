#input kalimat bebas
kalimat = input("Masukkan kata: ")

for i in range(1, len(kalimat) + 1):
    print(kalimat[:i])
