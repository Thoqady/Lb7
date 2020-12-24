#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#. Написать программу, которая считывает английский текст из файла и выводит на экран
#слова текста, начинающиеся и оканчивающиеся на гласные буквы.

if __name__ == '__main__':
    with open("1.txt", "r") as f:
        contents = f.read().upper()
    letters = contents.split(" ")
    a = ["A", "E", "I", "O", "U", "Y"]
    print(letters)

    for letter in letters:
        if letter[0] in a and letter[-1] in a:
            print(letter)