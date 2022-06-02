# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Дано предложение. Удалить из него все буквы о, стоящие на нечетных местах.
"""

if __name__ == '__main__':
    s = input("Напишите предложение: ")

    print(''.join(char for n, char in enumerate(
        s) if not (char == 'о' and n % 2 == 0)))
