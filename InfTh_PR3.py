# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 10:52:00 2023

@author: Ich
"""
import math

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

probabilities = Z_statistik("Test.txt")

w = "bade"

with open("Test.txt", 'r', encoding="utf-8") as file:
    w = file.read()
    
num_keys = [] 


def Q_ACencoder(word):
    low = 0    
    high = 1
    
    prev_start = 0
    
    num_keys = [] 
    
    for c in word:
        if c == '_':
            print("Interval für '",word[:len(word)-1],"' ist [",low,";",high,")")
            return
        start = prev_start
        delta = high - low
        
        
        print("low -> ",low)
        for a,p in probabilities.items():
            prev_start = start
            
            start = (start + delta * p)
            
            print("[",(prev_start),";",(start),"] -> ", a)
            if c == a:
                #word += a
                high = start
                low = prev_start
                start = prev_start
                break
            
        print("high -> ",high)
    
    print((low+high)/2)
    
    return (low+high)/2
            

            
               
        
#        start = prev_start + delta * p[w]

def Q_ACdecoder(code):
    low = 0    
    high = 1
    
    prev_start = 0
    
    stop = False
    build = ""
    
    num_keys = [] 
    
    
    
    while not (high+low)/2 == code:
        start = prev_start
        delta = high - low
        
        
        #print("low -> ",low)
        for a,p in probabilities.items():
            prev_start = start
            start = (start + delta * p)
            
            if prev_start <= code and start > code:
                build += a
                high = start
                low = prev_start
                start = prev_start
                break
        
        #print("high -> ",high)
        print("WORD: ", build, " Prob: ", (high+low)/2 - code)
        

enc = Q_ACencoder(w)
dec = Q_ACdecoder(enc)
#print(Z_statistik("Test.txt"))

