#-*- coding: utf-8 -*-
import json
import unittest
from .constants import CONST
from .conf.config import appid, appsecret

from pywechat import WechatService
from pywechat.excepts import WechatError
from pywechat.services.basic import Basic


class TestCase(unittest.TestCase):
    '''Creates a TestCase template to help test.'''

    def setUp(self):
        self.service = WechatService(appid, appsecret)


class BasicTest(unittest.TestCase):
    '''Creates a TestCase for the class of Basic.'''

    def setUp(self):
        self.basic = Basic(appid, appsecret)

    def test_check_wechat_error(self):
        errcode = CONST.NUMBER
        errmsg = CONST.STRING
        data = {
            "errcode": errcode,
            "errmsg": errmsg
        }
        with self.assertRaises(WechatError) as e:
            self.basic._check_wechat_error(data)
        exception = e.exception
        self.assertEqual(exception.code, errcode)
        self.assertEqual(exception.message, errmsg)


