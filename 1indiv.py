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

        if (letter[0] == "A" or letter[0] == "E" or letter[0] == "I" or letter[0] == "O"
                or letter[0] == "U"
                or letter[0] == "Y"):
                    if (letter[-1] == "A"
                    or letter[-1] == "E" or letter[-1] == "I"
                    or letter[-1] == "O" or letter[-1] == "U" or letter[-1] == "Y"):

                         print(letter)


