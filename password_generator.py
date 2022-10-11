#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

char = \
    '0123456789abcdefghijkmnopqrstuvwxyzABCDEFGHIJKMNOpQRSTUVWXYZ@#$%=:?./|~>*()<'
number = input('enter number of password to be generated')
number = int(number)
length = input('enter length of passowrd')
length = int(length)
for i in range(number):
    passwords = ''
    for j in range(length):
        passwords += random.choice(char)
    print passwords

