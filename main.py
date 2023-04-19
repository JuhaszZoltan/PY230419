from module import *

koszones('Zoli')

egyik_szam:int = int(input('egyik szám: '))
masik_szam:int = int(input('másik szám: '))
ket_szam_osszege:int = osszadas(egyik_szam, masik_szam)
print(f'a két szám összge: {ket_szam_osszege}')

y:int = 20
x:int = 10
print(f'x + y = {osszadas(y, x)}')

print(f'11 + 33 = {osszadas(11, 33)}')

elkoszones()