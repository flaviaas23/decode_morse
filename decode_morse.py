#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Program to decode Morse code into text.
'''
__author__ = "Flavia A. Schneider"


import sys
import os
import re

def morse_code_to_text(morse_code: str) -> str:
    morse_dict = {
        ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", 
        ".": "E", "..-.": "F", "--.": "G", "....": "H", 
        "..": "I", ".---": "J", "-.-": "K", ".-..": "L", 
        "--": "M", "-.": "N", "---": "O", ".--.": "P", 
        "--.-": "Q", ".-.": "R", "...": "S", "-": "T", 
        "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
        "-.--": "Y", "--..": "Z",
        ".----": "1", "..---": "2", "...--": "3",
        "....-": "4", ".....": "5", "-....": "6",
        "--...": "7", "---..": "8", "----.": "9",
        "-----": "0"
    }
    # Remove espaços extras no início/fim e padroniza separação entre palavras
    morse_code = morse_code.strip()
    
    # Divide as palavras por 3 ou mais espaços
    words = re.split(r'\s{3,}', morse_code)

    decoded_message = []
    
    for word in words:
        letters = word.strip().split()
        decoded_word = ''.join(morse_dict.get(letter, '') for letter in letters)
        decoded_message.append(decoded_word)
    
    return ' '.join(decoded_message)

def main():

    if len(sys.argv) < 2:
        nome_prog = os.path.basename(__file__)
        print(f"Uso: python {nome_prog} '<morse code>'")
        sys.exit(1)
    morse_code = sys.argv[1]
    decoded_text = morse_code_to_text(morse_code)
    print(decoded_text)

if __name__ == "__main__":
    main()