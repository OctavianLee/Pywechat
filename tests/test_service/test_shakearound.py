#-*- coding: utf-8 -*-
import json
import mock
import unittest
from nose.tools import eq_, ok_
from ..constants import CONST
from ..test_base import TestCase

from pywechat.services.basic import Basic
from pywechat.services.wechat_shake import ShakeService


class ShakeServiceTest(TestCase):

    '''Creates a TestCase for Shake Service.'''

    def setUp(self):
        TestCase.setUp(self)
        with mock.patch.object(Basic, 'access_token', autospec=True):
            self.shakeservice = self.service.init_service('Shake')

    def test_apply_devices(self):
        with mock.patch.object(ShakeService, 'apply_devices') as mock_method:
            apply_id = CONST.NUMBER
            device_id = CONST.NUMBER
            uuid = CONST.STRING
            major = CONST.NUMBER
            minor = CONST.NUMBER
            mock_method.return_value = {
                "data": {
                    "apply_id": apply_id,
                    "device_identifiers": [
                        {
                            "device_id": device_id,
                            "uuid": uuid,
                            "major": major,
                            "minor": minor
                        }
                    ]
                },
                "errcode": 0,
                "errmsg": "success."
            }
            apply_reason = CONST.STRING
            comment = CONST.STRING
            data = self.shakeservice.apply_devices(1,
                                                   apply_reason, comment)
            eq_(data["data"]["apply_id"], apply_id)
            eq_(data["data"]["device_identifiers"][0]["device_id"], device_id)
            eq_(data["data"]["device_identifiers"][0]["uuid"], uuid)
            eq_(data["data"]["device_identifiers"][0]["major"], major)
            eq_(data["data"]["device_identifiers"][0]["minor"], minor)
