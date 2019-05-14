#!/usr/bin/env python3

from tkinter import *
import math

class Calc:
    def add(self, a, b):
        result = a + b
        print("somme = ", result)
    def sub(self, a, b):
        result = a - b
        print("soustract = ", result)
    def multiple(self, a, b):
        result = a * b
        print("multiplication = ", result)
    def div(self, a, b):
        result = a/b
        print("division = ", result)
    def logneper(self, a):
        result = math.log(a)
        print("logarithme népérien = ", result)
    def tangente(self, a):
        result = math.tan(a)
        print("tangente = ", result)