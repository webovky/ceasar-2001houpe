#!/usr/bin/env python3
# Soubor:  caesar.py
# Datum:   02.10.2018 00:36
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
############################################################################

soubor = open('sifra.txt', encoding = 'utf-8')

obsah = soubor.read()

soubor.close()



def caesar():
    key = int(input("Zadejte klíč:"))
    plaintext = obsah
    zprava = ""
    for pismeno in plaintext:
        prevod=ord(pismeno)
        prevod=prevod + key
        if (prevod > ord("Z")):
            prevod = prevod - 26
        pismeno=chr(prevod)
        zprava = zprava + pismeno
    print(zprava)

caesar()


