#-*- coding: utf-8 -*-
import json
import mock
import unittest
from nose.tools import eq_, ok_
from .constants import CONST

from pywechat import WechatService
from pywechat.excepts import WechatError
from pywechat.services.basic import Basic


class TestCase(unittest.TestCase):
    '''Creates a TestCase template to help test.'''

    def setUp(self):
        self.service = WechatService(CONST.STRING, CONST.STRING)


class BasicTest(unittest.TestCase):
    '''Creates a TestCase for the class of Basic.'''

    def setUp(self):
        with mock.patch.object(Basic, 'access_token', autospec=True):
            self.basic = Basic(CONST.STRING, CONST.STRING)

    def test_check_wechat_error(self):
        '''Tests the _check_wechat_error method.'''
        errcode = CONST.NUMBER
        errmsg = CONST.STRING
        data = {
            "errcode": errcode,
            "errmsg": errmsg
        }
        with self.assertRaises(WechatError) as e:
            self.basic._check_wechat_error(data)
        exception = e.exception
        eq_(exception.code, errcode)
        eq_(exception.message, errmsg)

    def test_send_request(self):
        '''Tests the _send_request  method.'''
        with mock.patch.object(Basic, '_send_request'):
            ok_(self.basic._send_request('get', CONST.STRING))
            ok_(self.basic._send_request('post', CONST.STRING))

    def test_grant_access_token(self):
        '''Tests the _grant_access_token method.'''
        with mock.patch.object(Basic, '_send_request') as mock_method:
            access_token = CONST.STRING
            expires_in = CONST.NUMBER
            mock_method.return_value = {
              "access_token": access_token,
              "expires_in": expires_in
            }
            data = self.basic._grant_access_token()
            eq_(data.get('access_token'), access_token)
            eq_(data.get('expires_in'), expires_in)

    def test_get_wechat_server_ips(self):
        '''Tests the _get_wechat_server_ips method.'''
        with mock.patch.object(Basic, '_send_request') as mock_method:
            with mock.patch.object(Basic, '_grant_access_token') as method:
                ips = [CONST.STRING] * CONST.NUMBER
                method.return_value = CONST.STRING
                mock_method.return_value = {
                  "ips": ips
                }
                data = self.basic._get_wechat_server_ips()
                eq_(data.get('ips'), ips)
