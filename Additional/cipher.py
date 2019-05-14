# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re

def modify(text):
    text = re.sub(r'[^a-zA-Z]', '', text)
    text = text.lower()
    return text

def cezar(text, move):
    toReturn = ""
    for i in text:
        if ord(i) + move > 122:
            toReturn += chr(ord(i) + move - 26)
        else:
            toReturn += chr(ord(i) + move)
            
    return toReturn
    
def deCezar(text, move):
    toReturn = ""
    for i in text:
        if ord(i) - move < 97:
            toReturn += chr(ord(i) - move + 26)
        else:
            toReturn += chr(ord(i) - move)
            
    return toReturn
    
def podstawieniowy(text, alfabet):
    return text.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", alfabet))
    
def dePodstawieniowy(text, alfabet):
    return text.translate(str.maketrans(alfabet, "abcdefghijklmnopqrstuvwxyz"))
    
def zKluczem(text, klucz):
    toReturn = ""
    move = []
    klucz = modify(klucz)
    for i in klucz:
        move.append("abcdefghijklmnopqrstuvwxyz".index(i) + 1)
    
    x = 0 #Indicates which elemt of move[] use
    for i in text:
        toReturn += cezar(i, move[x % 3])
        x += 1
        
    return toReturn
    
def deZKluczem(text, klucz):
    toReturn = ""
    move = []
    klucz = modify(klucz)
    for i in klucz:
        move.append("abcdefghijklmnopqrstuvwxyz".index(i) + 1)
    
    x = 0 #Indicates which elemt of move[] use
    for i in text:
        toReturn += deCezar(i, move[x % 3])
        x += 1
        
    return toReturn
  
def main():          
    alphabet = "qazwsxplokmijnedcrfvuytghb"
    Text = "Tekst do zaszyfrowania!@# chyba?"
    print(Text)
    
    Text = modify(Text)
    print(Text)
    Text = cezar(Text, 13)
    print(Text)
    Text = deCezar(Text, 13)
    print(Text)
    print("")
    
    Text = podstawieniowy(Text, alphabet)
    print(Text)
    Text = dePodstawieniowy(Text, alphabet)
    print(Text)
    print("")
    
    Text = zKluczem(Text, "BOA")
    print(Text)
    Text = deZKluczem(Text, "BOA")
    print(Text)
    print("")
    
    
if __name__ == "__main__":
    main()