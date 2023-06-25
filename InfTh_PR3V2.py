# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 15:25:45 2023

@author: Ich
"""

import math
from decimal import Decimal


def Z_statistik(text_file):
    
    with open(text_file, 'r', encoding="utf-8") as file:
        text = file.read()
    
    # Mach mir eine Dictornary was das vorkommen dieses Zeichens zählt
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Berechnen der Gesamtanzahl an Zeichen im Text
    total_chars = sum(char_count.values())
    
    # Berechnen der Wahrscheinlichkeiten jedes Zeichens und des Informationsgehalts jedes Zeichens
    probs = {}
    info_content = {}
    for char, count in char_count.items():
        probs[char] = Decimal(count) / Decimal(total_chars)
        
    return probs
    
    # Ausgabe der Entropie des Textes
   # print("Entropie des Textes:", entropy)

#probabilities = { 'a': 1/2, 'b': 1/4, 'c': 1/8, 'd': 1/16, 'e': 1/16 }
probabilities = Z_statistik("Test.txt")
#w = "bade"

with open("Test.txt", 'r', encoding="utf-8") as file:
    w = file.read()


def Q_ACencoder(word):
    low = 0
    high = 1
    
    prev_start = low
    
    counter = 0
    builder = []
    
    for c in word:
        start = prev_start
        delta = high - low
        
        for a,p in probabilities.items():
            prev_start = start
            start = Decimal(start) + Decimal(delta) * Decimal(p)
            
            print("P: ",prev_start)
            print("S: ",start)
            
            if c != a:
                continue
            
            print(a, (prev_start+start)/2)
            
            
            
            if counter != 0 and counter % 20 == 0:
                builder.append(Decimal((low+high)/2))
                prev_start = 0
                start = 1
            
            counter = counter + 1
            
            
            low = prev_start
            high = start
            start = prev_start
            break
    
    builder.append(Decimal((low+high)/2))
    
    return builder



    

def Q_ACdecoder(code):
    low = 0
    high = 1
    
    build_word = ""
    
    counter = 0
    
    for c in code:
        
        prev_start = 0
        start = 1
        
        low = prev_start
        high = start
        start = prev_start
        
        while c != Decimal((high+low)/2):
            start = prev_start
            delta = high - low
        
            for a,p in probabilities.items():
                prev_start = start
                start = Decimal(start) + Decimal(delta) * Decimal(p)
            
                if not(prev_start <= c and start > c):
                    continue
                
                print(build_word)
                build_word += a
                
                
                
                
                if counter != 0 and counter % 20 == 0:
                    prev_start = 0
                    start = 1
                
                counter = counter + 1
                
                
                low = prev_start
                high = start
                start = prev_start
                break    
    
    return build_word
            
                


enc = Q_ACencoder(w)
print(enc)
dec = Q_ACdecoder(enc)
print(dec)























