from MinuOmaModul1 import *

failide_kustutamine()

ümber_kirjuta_fail(input("Faili nimi: "))

kirjuta_failisse("Päevad1.txt")

päevad=loe_failist("Päevad1.txt")
print(päevad)
for päev in päevad:
    print(päev)
