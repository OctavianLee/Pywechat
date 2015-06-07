# -*- coding: utf-8 -*-
from utils import constant, get_random_str, get_random_int

class _Constant(object):

    @constant
    def NUMBER():
        return get_random_int()

    @constant
    def STRING():
        return get_random_str(10)


CONST = _Constant()
