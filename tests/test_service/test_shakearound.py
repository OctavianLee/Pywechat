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

    def test_update_device(self):
        comment = CONST.STRING
        device_id = CONST.NUMBER
        uuid = CONST.NUMBER
        major = CONST.NUMBER
        minor = CONST.NUMBER
        with mock.patch.object(ShakeService, 'update_device') as mock_method:
            mock_method.return_value = {
                "data": {
                },
                "errcode": 0,
                "errmsg": "success."
            }
            data = self.shakeservice.update_device(comment, device_id)
            self.assertIsNotNone(data)
            data = self.shakeservice.update_device(comment, uuid=uuid,
                                                   major=major, minor=minor)
            self.assertIsNotNone(data)

    def test_bind_location(self):
        poi_id = CONST.NUMBER
        device_id = CONST.NUMBER
        uuid = CONST.NUMBER
        major = CONST.NUMBER
        minor = CONST.NUMBER
        with mock.patch.object(ShakeService, 'bind_location') as mock_method:
            mock_method.return_value = {
                "data": {
                },
                "errcode": 0,
                "errmsg": "success."
            }
            data = self.shakeservice.bind_location(poi_id, device_id)
            self.assertIsNotNone(data)
            data = self.shakeservice.bind_location(poi_id, uuid=uuid,
                                                   major=major, minor=minor)
            self.assertIsNotNone(data)

    def test_search_device(self):
        device_id = CONST.NUMBER
        uuid = CONST.NUMBER
        major = CONST.NUMBER
        minor = CONST.NUMBER
        with mock.patch.object(ShakeService, 'search_device') as mock_method:
            mock_method.return_value = {
                "data": {
                    "devices": [
                        {
                            "comment": "",
                            "device_id": device_id,
                            "major": major,
                            "minor": minor,
                            "page_ids": "15369",
                            "status": 1,
                            "poi_id": 0,
                            "uuid": uuid
                        }
                    ],
                    "total_count": 1
                },
                "errcode": 0,
                "errmsg": "success."
            }
            data = self.shakeservice.search_device(device_id)
            eq_(data["data"]["devices"][0]["device_id"], device_id)
            eq_(data["data"]["devices"][0]["uuid"], uuid)
            eq_(data["data"]["devices"][0]["major"], major)
            eq_(data["data"]["devices"][0]["minor"], minor)
            data = self.shakeservice.search_device(uuid=uuid,
                                                   major=major, minor=minor)
            eq_(data["data"]["devices"][0]["device_id"], device_id)
            eq_(data["data"]["devices"][0]["uuid"], uuid)
            eq_(data["data"]["devices"][0]["major"], major)
            eq_(data["data"]["devices"][0]["minor"], minor)

    def test_search_devices(self):
        apply_id = CONST.NUMBER
        device_id = CONST.NUMBER
        uuid = CONST.NUMBER
        major = CONST.NUMBER
        minor = CONST.NUMBER
        with mock.patch.object(ShakeService, 'search_devices') as mock_method:
            mock_method.return_value = {
                "data": {
                    "devices": [
                        {
                            "comment": "",
                            "device_id": device_id,
                            "major": major,
                            "minor": minor,
                            "page_ids": "15369",
                            "status": 1,
                            "poi_id": 0,
                            "uuid": uuid
                        }
                    ],
                    "total_count": 1
                },
                "errcode": 0,
                "errmsg": "success."
            }
            data = self.shakeservice.search_devices(0, 1, apply_id)
            eq_(data["data"]["devices"][0]["device_id"], device_id)
            eq_(data["data"]["devices"][0]["uuid"], uuid)
            eq_(data["data"]["devices"][0]["major"], major)
            eq_(data["data"]["devices"][0]["minor"], minor)
            eq_(data["data"]["total_count"], 1)

    def test_upload_material(self):
        image = CONST.STRING
        pic_url = CONST.STRING
        with mock.patch.object(ShakeService, 'upload_material') as mock_method:
            mock_method.return_value = {
                "data": {
                    "pic_url": pic_url
                },
                "errcode": 0,
                "errmsg": "success."
            }
            data = self.shakeservice.upload_material(image)
            eq_(data["data"]["pic_url"], pic_url)

    def test_add_page(self):
        title = CONST.STRING
        description = CONST.STRING
        page_url = CONST.STRING
        icon_url = CONST.STRING
        comment = CONST.STRING
        page_id = CONST.NUMBER
        with mock.patch.object(ShakeService, 'add_page') as mock_method:
            mock_method.return_value = {
                "data": {
                    "page_id": page_id
                },
                "errcode": 0,
                "errmsg": "success."
            }
            data = self.shakeservice.add_page(title, description, page_url,
                                              icon_url, comment)
            eq_(data["data"]["page_id"], page_id)
