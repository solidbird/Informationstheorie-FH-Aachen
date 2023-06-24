import math
import re


def Z_statistik(text_file):
    
    with open(text_file, 'r') as file:
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
    print("Buchstaben und deren Informationsgehalt:")
    for char, info in info_content.items():
        print(char, info)
    
    # Berechnen der Entropie des Textes
    entropy = sum(probs[char] * info_content[char] for char in char_count)
    
    # Ausgabe der Entropie des Textes
    print("Entropie des Textes:", entropy)

def Z2_statistik(text_file):
    with open(text_file, 'r') as file:
        text = file.read()
        
    tup_count = {}
    for i in range(len(text)-1):
        tup = text[i:i+2]
        if tup in tup_count:
            tup_count[tup] += 1
        else:
            tup_count[tup] = 1
    
    total_tups = sum(tup_count.values())
    
    probs = {}
    info_content = {}
    for tup, count in tup_count.items():
        probs[tup] = count / total_tups
        info_content[tup] = -math.log2(probs[tup])
    
    print("Zeichentupel und deren Informationsgehalt:")
    for tup, info in info_content.items():
        print(tup, info)
    
    entropy = sum(probs[tup] * info_content[tup] for tup in tup_count)
    
    print("Entropie der Zeichentupel-Menge:", entropy)

def W_statistik(text_file):
    with open(text_file, 'r') as file:
        text = file.read()
    
    words = re.findall(r'\w+', text)
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    total_words = sum(word_count.values())
    
    probs = {}
    info_content = {}
    for word, count in word_count.items():
        probs[word] = count / total_words
        info_content[word] = -math.log2(probs[word])
    
    print("Wörter und deren Informationsgehalt:")
    for word, info in info_content.items():
        print(word, info)
    
    entropy = sum(probs[word] * info_content[word] for word in word_count)
    
    print("Entropie der Wortmenge:", entropy)


file = "Test.txt"

print("\n\nAufgabe a)")
Z_statistik(file)

print("\n\nAufgabe b)")
Z2_statistik(file)

print("\n\nAufgabe c)")
W_statistik(file)


