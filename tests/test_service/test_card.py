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
