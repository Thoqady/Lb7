#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#. Написать программу, которая считывает английский текст из файла и выводит на экран
#слова текста, начинающиеся и оканчивающиеся на гласные буквы.

if __name__ == '__main__':
    with open("1.txt", "r") as f:
        contents = f.read().upper()
    sentences = contents.split(" ")
    a = ["A", "E", "I", "O", "U", "Y"]
    print(sentences)

    for sentence in sentences:

        if (sentence[0] == "A" or sentence[0] == "E" or sentence[0] == "I" or sentence[0] == "O"
                or sentence[0] == "U"
                or sentence[0] == "Y"):
                    if (sentence[-1] == "A"
                     or sentence[-1] == "E" or sentence[-1] == "I"
                     or sentence[-1] == "O" or sentence[-1] == "U" or sentence[-1] == "Y"):

                         print(sentence)


