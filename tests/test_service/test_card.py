#-*- coding: utf-8 -*-
import json
import mock
import unittest
from nose.tools import eq_, ok_
from ..constants import CONST
from ..test_base import TestCase

from pywechat.services.basic import Basic
from pywechat.services.wechat_card import CardService


class CardServiceTest(TestCase):

    '''Creates a TestCase for Card Service.'''

    def setUp(self):
        TestCase.setUp(self)
        with mock.patch.object(Basic, 'access_token', autospec=True):
            self.card_service = self.service.init_service('Card')

    def test_get_colors(self):
        with mock.patch.object(CardService, 'get_colors') as mock_method:
            mock_method.return_value = {
                "colors": [
                    {"name": "Color010", "value": "#55bd47"},
                    {"name": "Color020", "value": "#10ad61"},
                    {"name": "Color030", "value": "#35a4de"},
                    {"name": "Color040", "value": "#3d78da"},
                    {"name": "Color050", "value": "#9058cb"},
                    {"name": "Color060", "value": "#de9c33"},
                    {"name": "Color070", "value": "#ebac16"},
                    {"name": "Color080", "value": "#f9861f"},
                    {"name": "Color081", "value": "#f08500"},
                    {"name": "Color090", "value": "#e75735"},
                    {"name": "Color100", "value": "#d54036"},
                    {"name": "Color101", "value": "#cf3e36"}
                ],
                "errcode": 0,
                "errmsg": "success."
            }
            data = self.card_service.get_colors()
            self.assertIsNotNone(data["colors"])

    def test_upload_image(self):
        image = CONST.STRING
        pic_url = CONST.STRING
        with mock.patch.object(CardService, 'upload_image') as mock_method:
            mock_method.return_value = {
                "url": pic_url
            }
            data = self.card_service.upload_image(image)
            eq_(data["url"], pic_url)

    def test_unavilable_code(self):
        code = CONST.STRING
        card_id = CONST.STRING
        openid = CONST.STRING
        with mock.patch.object(CardService, 'unavailable_code') as mock_method:
            mock_method.return_value = {
                "errcode": 0,
                "errmsg": "ok",
                "card": {"card_id": card_id},
                "openid": openid

            }
            data = self.card_service.unavailable_code(code, card_id)
            eq_(data["card"]["card_id"], card_id)
            eq_(data["openid"], openid)

    def test_decrypt_code(self):
        encrypt_code = CONST.STRING
        card_id = CONST.STRING
        openid = CONST.STRING
        with mock.patch.object(CardService, 'decrypt_code') as mock_method:
            mock_method.return_value = {
                "errcode": 0,
                "errmsg": "ok",
                "card": {"card_id": card_id},
                "openid": openid

            }
            data = self.card_service.decrypt_code(encrypt_code)
            eq_(data["card"]["card_id"], card_id)
            eq_(data["openid"], openid)

    def test_get_code(self):
        code = CONST.STRING
        card_id = CONST.STRING
        begin_time = CONST.NUMBER
        end_time = CONST.NUMBER
        openid = CONST.STRING
        with mock.patch.object(CardService, 'get_code') as mock_method:
            mock_method.return_value = {
                "errcode": 0,
                "errmsg": "ok",
                "card": {
                    "card_id": card_id,
                    "begin_time": begin_time,
                    "end_time": end_time,
                },
                "openid": openid

            }
            card_data = {
                "card_id": card_id,
                "begin_time": begin_time,
                "end_time": end_time,
            }
            data = self.card_service.get_code(code, card_id)
            eq_(data["card"], card_data)
            eq_(data["openid"], openid)

    def test_batchget_code(self):
        card_id = CONST.STRING
        with mock.patch.object(CardService, 'batchget_card') as mock_method:
            mock_method.return_value = {
                "errcode": 0,
                "errmsg": "ok",
                "card_id_list": [card_id],
                "total_num": 1
            }
            data = self.card_service.batchget_card(0, 1)
            eq_(data["card_id_list"][0], card_id)
            eq_(data["total_num"], 1)

    def test_modify_stock(self):
        card_id = CONST.STRING
        increase_stock_value = CONST.NUMBER
        reduce_stock_value = CONST.NUMBER

        with mock.patch.object(CardService, 'modify_stock') as mock_method:
            mock_method.return_value = {
                "errcode": 0,
                "errmsg": "ok",
            }
            data = self.card_service.modify_stock(card_id,
                                                  increase_stock_value, reduce_stock_value)
            self.assertIsNotNone(data)

    def test_update_code(self):
        code = CONST.STRING
        new_code = CONST.STRING
        card_id = CONST.STRING

        with mock.patch.object(CardService, 'update_code') as mock_method:
            mock_method.return_value = {
                "errcode": 0,
                "errmsg": "ok",
            }
            data = self.card_service.update_code(code, new_code, card_id)
            self.assertIsNotNone(data)

    def test_delete_card(self):
        card_id = CONST.STRING

        with mock.patch.object(CardService, 'delete_card') as mock_method:
            mock_method.return_value = {
                "errcode": 0,
                "errmsg": "ok",
            }
            data = self.card_service.delete_card(card_id)
            self.assertIsNotNone(data)
