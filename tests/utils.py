# -*- coding: utf-8 -*-
import string
import random


def constant(fn):
    def fset(self, value):
        raise SyntaxError
    def fget(self):
        return fn()
    return property(fget, fset)

def get_random_str(n):
    elements = string.letters + string.digits
    result = random.sample(elements, n)
    if result[0].isdigit():
        result = result[1:]
    return ''.join(result)

def get_random_int():
    return random.randint(0, 999999)

