import os

from exercice1 import *
path = "programme-a-obfusquer.txt"

dictionnaire_corrige: dict = {
    '//[0x61]': 'a', '//[0x62]': 'b', '//[0x63]': 'c', '//[0x64]': 'd', '//[0x65]': 'e', '//[0x66]': 'f',
    '//[0x67]': 'g', '//[0x68]': 'h', '//[0x69]': 'i', '//[0x6a]': 'j', '//[0x6b]': 'k', '//[0x6c]': 'l',
    '//[0x6d]': 'm', '//[0x6e]': 'n', '//[0x6f]': 'o', '//[0x70]': 'p', '//[0x71]': 'q', '//[0x72]': 'r',
    '//[0x73]': 's', '//[0x74]': 't', '//[0x75]': 'u', '//[0x76]': 'v', '//[0x77]': 'w', '//[0x78]': 'x',
    '//[0x79]': 'y', '//[0x7a]': 'z', '//[0x41]': 'A', '//[0x42]': 'B', '//[0x43]': 'C', '//[0x44]': 'D',
    '//[0x45]': 'E', '//[0x46]': 'F', '//[0x47]': 'G', '//[0x48]': 'H', '//[0x49]': 'I', '//[0x4a]': 'J',
    '//[0x4b]': 'K', '//[0x4c]': 'L', '//[0x4d]': 'M', '//[0x4e]': 'N', '//[0x4f]': 'O', '//[0x50]': 'P',
    '//[0x51]': 'Q', '//[0x52]': 'R', '//[0x53]': 'S', '//[0x54]': 'T', '//[0x55]': 'U', '//[0x56]': 'V',
    '//[0x57]': 'W', '//[0x58]': 'X', '//[0x59]': 'Y', '//[0x5a]': 'Z', '//[0x30]': '0', '//[0x31]': '1',
    '//[0x32]': '2', '//[0x33]': '3', '//[0x34]': '4', '//[0x35]': '5', '//[0x36]': '6', '//[0x37]': '7',
    '//[0x38]': '8', '//[0x39]': '9', '//[0x28]': '(', '//[0x29]': ')', '//[0x2e]': '.', '//[0x22]': '"',
    '//[0x20]': ' ', '//[0x2f]': '/', '//[0x3d]': '=', '//[0x3a]': ':', '//[0x3b]': ';', '//[0x3c]': '<',
    '//[0x3e]': '>', '//[0x5f]': '_', '//[0x2d]': '-', '//[0x5c]': '\\', '//[0x2b]': '+', '//[0x2c]': ',',
    '//[0x27]': "'", '//[0x7b]': '{', '//[0x7d]': '}', '//[0x23]': '#', '//[0x2a]': '*', '//[0x5b]': '[',
    '//[0x5d]': ']', '//[0x7F]': '', '//[0x00]': '', '//[0x07]': '', '//[0x1E]': '', '_ZN4ctrl1iC1Ev': 'if',
    '_ZN4ctrl1eC1Ev': 'else', '_ZN4ctrl1wC1Ev': 'while', '_ZN4ctrl1fC1Ev': 'for', '_ZN4ctrl1rC1Ev': 'range',
    '_ZN4ctrl1tC1Ev': 'try', '_ZN4ctrl1xC1Ev': 'except', '_ZN4util1iC1Ev': 'import', '//[0x0a]': '\n',
    '_ZN4util1fC1Ev': 'from', '_ZN3doc1tC1Ev': '__title__', '_ZN3doc1aC1Ev': '__author__',
    '_ZN3doc1cC1Ev': '__copyright__', '_ZN4cond1nC1Ev': 'not', '_ZN4cond1aC1Ev': 'and', '_ZN4cond1sC1Ev': 'as',
    '_ZN4spec1pC1Ev': '+=', '_ZN4spec1mC1Ev': '-=', "_ZN4ctrl1vC1Ev": '', "_ZN4util1jC1Ev": '', "_ZN3doc1bC1Ev": '',
    "_ZN4cond1mC1Ev": '', "_ZN4spec1qC1Ev": ''
}

print(charger_contenu(path))
print(creer_dictionnaire())
print(set(creer_dictionnaire()).difference(dictionnaire_corrige))
transpilation("programme-obfusque.txt", "test.txt")