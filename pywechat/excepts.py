# -*- coding: utf-8 -*-


class WechatError(Exception):

    '''An exception of the wechat error.'''

    def __init__(self, code, message=None):
        Exception.__init__(self)
        self.code = code
        self.message = message

    def __str__(self):
        return '{0}: {1}'.format(self.code, self.message)


class CodeBuildError(Exception):

    '''An exception of Pywechat'''

    def __init__(self, message=None):
        Exception.__init__(self)
        self.message = message

    def __str__(self):
        return '{0}'.format(self.message)
