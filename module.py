from time import sleep
from os import system

def osszadas (x:int, y:int) -> int:
    osszeg:int = x + y
    return osszeg


def koszones(nev:str) -> None:
    print(f'Szia, {nev}!')
    valasz:str = input('Milyen napod van? ')
    if valasz == 'szar':
        print('Sajnálattal hallom :(')
    elif 'jó' in valasz:
        print('örülök, akkor lássunk neki!')
    else: print('jó munkát!')


def elkoszones() -> None:
    print('örülök, hogy ma is találkoztunk!')
    print('viszont látásra!')
    sleep(2)
    for x in range(3):
        system('cls')
        print(3 - x, end='')
        for y in range(3):
            print('.', end='')
            sleep(.5)
    print("===A PROGRAMNAK VÉGE===")