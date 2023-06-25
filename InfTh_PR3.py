# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 10:52:00 2023

@author: Ich
"""
import math
from decimal import Decimal

def safe_floating_num(num):
    pass

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
        probs[char] = count / total_chars
        info_content[char] = -math.log2(probs[char])
        
    # Ausgabe der Buchstaben und deren Informationsgehalt
    #print("Buchstaben und deren Informationsgehalt:")
    for char, info in info_content.items():
        print(char, info)
    
    # Berechnen der Entropie des Textes
    entropy = sum(probs[char] * info_content[char] for char in char_count)
    
    return probs
    
    # Ausgabe der Entropie des Textes
   # print("Entropie des Textes:", entropy)

#probabilities = { 'a': 1/2, 'b': 1/4, 'c': 1/8, 'd': 1/16, 'e': 1/16 }
probabilities = Z_statistik("Test.txt")
probabilities = dict(sorted(probabilities.items()))
w = "bade"

with open("Test.txt", 'r', encoding="utf-8") as file:
    w = file.read()
    
num_keys = [] 


def Q_ACencoder(word):
    low = 0    
    high = 1
    
    prev_start = 0
    
    builder = "" 
    counter = 0
    
    lol = ""
    
    for c in word:

        start = prev_start
        delta = high - low
        
        
        print("low -> ",low)
        for a,p in probabilities.items():
            prev_start = start
            
            start = Decimal(start) + Decimal(delta) * Decimal(p)
            #start = start + delta * p
            
            print("[",(prev_start),";",(start),"] -> ", a)
            if c == a:
                counter = counter + 1
                lol += c
                print("AAAAAAAAAAAAAAAA: ", lol)
                
                if counter % 20 == 0:
                    builder += str((low+high)/2)
                    prev_start = 0
                    start = 1
                                    
                #word += a
                high = start
                low = prev_start
                start = prev_start
                break
            
        print("high -> ",high)
        
    print((low+high)/2)
    
    
    builder += str((low+high)/2)
    return builder 
            

            
               
        
#        start = prev_start + delta * p[w]

def Q_ACdecoder(code):
    index = 0
    counter = 0
    
    low = 0    
    high = 1
    
    prev_start = 0
    
    nums=[Decimal("0." + x) for x in code.split("0.")]
    nums=nums[1:len(nums)]
    
    num = 0    
    
    word_builder = ""
    
    while nums[-1] != num:
        
        start = prev_start
        delta = high - low
        
        for a,p in probabilities.items():
            prev_start = start
            
            start = Decimal(start) + Decimal(delta) * Decimal(p)
            debug_start = float(start)
            debug_prev_start = float(prev_start)
            debug_num = float(nums[index])
            
            
            if nums[index] == (prev_start+start)/2:
                num = (prev_start+start)/2
                word_builder += a
                
                
                
                
                if counter % 20 == 0:
                    index = index + 1
                    prev_start = 0
                    start = 1
                
                break
            
            
            if prev_start <= nums[index] and start > nums[index]:
                
                
                high = start
                low = prev_start
                start = prev_start
             
                
            

    return word_builder
    
    
enc = Q_ACencoder(w)
print(enc)
dec = Q_ACdecoder(enc)
print(dec)
#print(Z_statistik("Test.txt"))

