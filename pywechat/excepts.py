# -*- coding: utf-8 -*-


class WechatError(Exception):
    '''An exception of the wechat error.'''
    def __init__(self, code, message=None):
        self.code = code
        self.message = message

    def __str__(self):
        return '{0}: {1}'.format(self.code, self.message)

class SystemError(Exception):
    '''An exception of Pywechat'''
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        return '{0}'.format(self.message)
