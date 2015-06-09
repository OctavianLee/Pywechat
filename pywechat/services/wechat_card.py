# -*- coding: utf-8 -*-
from pywechat.services.basic import Basic

class CardService(Basic):
    """This class is an implement of the Wechat service of card.


    All request's urls come from the official documents.
    Link: https://mp.weixin.qq.com/wiki/home/index.html
    """

    def upload_image(self, image):
        """Uploads the image for the logo of card.

        Link:
        https://mp.weixin.qq.com/wiki/8/b7e310e7943f7763450eced91fa793b0.html

        Args:
            image: the file of image. open(image_name, 'rb')

        Returns:
            the json data.Example:
            {"url":"http://mmbiz.qpic.cn/mmbiz/iaL1LJM1mF9aRKPZJkm/0"}

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        url = 'https://api.weixin.qq.com/cgi-bin/media/uploadimg'
        files = {'buffer': image}
        json_data = self._send_request('post', url, files=files)
        return json_data
        
    def get_colors(self):
        """Gets the available colors of cards.

        Link:
        https://mp.weixin.qq.com/wiki/8/b7e310e7943f7763450eced91fa793b0.html

        Returns:
            the json data.Example:
            {
                "errcode":0,
                "errmsg":"ok",
                "colors":[
                    {"name":"Color010","value":"#55bd47"},
                    {"name":"Color020","value":"#10ad61"},
                    {"name":"Color030","value":"#35a4de"},
                    {"name":"Color040","value":"#3d78da"},
                    {"name":"Color050","value":"#9058cb"},
                    {"name":"Color060","value":"#de9c33"},
                    {"name":"Color070","value":"#ebac16"},
                    {"name":"Color080","value":"#f9861f"},
                    {"name":"Color081","value":"#f08500"},
                    {"name":"Color090","value":"#e75735"},
                    {"name":"Color100","value":"#d54036"},
                    {"name":"Color101","value":"#cf3e36"}
                ]
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        url = 'https://api.weixin.qq.com/card/getcolors'
        json_data = self._send_request('get', url)
        return json_data

    def create_card(
        self, card_dict, card_type, date_info,
        logo_url, code_type, brand_name, title,
        color, notice, description, quantity,
        **infos):
        """Creates a card.

        Link:
        https://mp.weixin.qq.com/wiki/8/b7e310e7943f7763450eced91fa793b0.html

        Returns:
            the json data.Example:
            { 
                "card": {
                    "card_type": "GROUPON",
                    "groupon": {
                        "base_info": {
                            "logo_url":  "http://mmbiz.qpic.cn/mmbiz/iaL1LJM1mF9aRK/0",
                            "brand_name":"海底捞",
                            "code_type":"CODE_TYPE_TEXT",
                            "title": "132元双人火锅套餐",
                            "sub_title": "周末狂欢必备",
                            "color": "Color010",
                            "notice": "使用时向服务员出示此券",
                            "service_phone": "020-88888888",
                            "description": "不可与其他优惠同享\n如需团购券发票，请在消费时向商户提出\n店内均可使用，仅限堂食",
                            "date_info": {
                                "type": 1,
                                "begin_timestamp": 1397577600,
                                "end_timestamp": 1422724261
                            },
                            "sku": {
                                "quantity": 50000000
                            },
                            "get_limit": 3,
                            "use_custom_code": false,
                            "bind_openid": false,
                            "can_share": true,
                            "can_give_friend": true,
                            "location_id_list": [123, 12321, 345345],
                            "custom_url_name": "立即使用",
                            "custom_url": "http://www.qq.com",
                            "custom_url_sub_title": "6个汉字tips",
                            "promotion_url_name": "更多优惠",
                            "promotion_url": "http://www.qq.com",
                            "source": "大众点评"   
                        },
                        "deal_detail":  "以下锅底2选1（有菌王锅、麻辣锅、大骨锅、番茄锅、清补凉锅、酸菜鱼锅可选）：\n大锅1份
                            12元\n小锅2份16元"}
                    }
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        base_info = {
            "logo_url": logo_url,
            "brand_name": brand_name,
            "title": title,
            "code_type": code_type,
            "color": color,
            "notice": notice,
            "description": description,
            "sku": {
                "quantity" : quantity
            },
            "date_info": date_info
        }
        base_info.update(infos)
        data = {
          "card": {
              "card_type": card_type.upper(),
              card_type.lower(): {
                  "base_info": base_info
              }
          }
        }
        data["card"][card_type].update(card_dict)

        url = 'https://api.weixin.qq.com/card/create'
        json_data = self._send_request('post', url, data=data)
        return json_data

    def create_qrcode(self, code, **infos):
        """Creates a qr code.

        (Link:
        https://mp.weixin.qq.com/wiki/12/ccd3aa0bddfe5211aace864de00b42e0.html)

        Returns:
            the json data.Example:
            {
              "errcode":0,
              "errmsg":"ok",
              "ticket":"gQG28DoAAAAAAAAAASxodHRwOi8vd2VpeGluLnFxLmN=="
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        card_dict = {
            "code": code
        }
        card_dict.update(infos)

        data = {
            "action_name": "QR_CARD",
            "action_info": {
                "card": {
                    card_dict
                }
            }
        }

        url = 'https://api.weixin.qq.com/card/qrcode/create'
        json_data = self._send_request('post', url, data=data)
        return json_data

    def unavailable_code(self, code, card_id=None):
        """Sets the code is unavailable.

        Link:
        https://mp.weixin.qq.com/wiki/5/3e7bccd4a8082733b2c86c3dcc9a636d.html

        Returns:
            the json data.Example:
            {
                "errcode":0,
                "errmsg":"ok",
                "card":{"card_id":"pFS7Fjg8kV1IdDz01r4SQwMkuCKc"},
                "openid":"oFS7Fjl0WsZ9AMZqrI80nbIq8xrA"
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        data = {
            "code": code
        }
        if card_id:
            data["card_id"] = card_id
        url = 'https://api.weixin.qq.com/card/code/unavailable'
        json_data = self._send_request('post', url, data=data)
        return json_data

    def decrypt_code(self, encrypt_code):
        """Decrypts the code.

        Link:
        https://mp.weixin.qq.com/wiki/5/3e7bccd4a8082733b2c86c3dcc9a636d.html

        Returns:
            the json data.Example:
            {
                "errcode":0,
                "errmsg":"ok",
                "card":{"card_id":"pFS7Fjg8kV1IdDz01r4SQwMkuCKc"},
                "openid":"oFS7Fjl0WsZ9AMZqrI80nbIq8xrA"
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        data = {
            "encrypt_code": encrypt_code
        }
        url = 'https://api.weixin.qq.com/card/code/decrtpt'
        json_data = self._send_request('post', url, data=data)
        return json_data

    def get_code(self, code, card_id=None):
        """Get the code.

        Link:
        https://mp.weixin.qq.com/wiki/3/3f88e06725fd911e6a46e2f5552d80a7.html

        Returns:
            the json data.Example:
            {
                "errcode":0,
                "errmsg":"ok",
                "openid":"oFS7Fjl0WsZ9AMZqrI80nbIq8xrA",
                "card":{
                    "card_id":"pFS7Fjg8kV1IdDz01r4SQwMkuCKc",
                    "begin_time": 1404205036,
                    "end_time": 1404205036,
                }
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        data = {
            "code": code
        }
        if card_id:
            data["card_id"] = card_id
        url = 'https://api.weixin.qq.com/card/code/get'
        json_data = self._send_request('post', url, data=data)
        return json_data

    def get_card(self, card_id):
        """Get the card.

        Link:
        https://mp.weixin.qq.com/wiki/3/3f88e06725fd911e6a46e2f5552d80a7.html

        Returns:
            the json data.Example:
            { 
                "card": {
                    "card_type": "GROUPON",
                    "groupon": {
                        "base_info": {
                            "logo_url":  "http://mmbiz.qpic.cn/mmbiz/iaL1LJM1mF9aRKPZJkmG8x/0",
                            "brand_name":"海底捞",
                            "code_type":"CODE_TYPE_TEXT",
                            "title": "132元双人火锅套餐",
                            "sub_title": "周末狂欢必备",
                            "color": "Color010",
                            "notice": "使用时向服务员出示此券",
                            "service_phone": "020-88888888",
                            "description": "不可与其他优惠同享\n如需团购券发票，请在消费时向商户提出\n店内均可使用，仅限堂食",
                            "date_info": {
                                "type": 1,
                                "begin_timestamp": 1397577600,
                                "end_timestamp": 1422724261
                            },
                            "sku": {
                                "quantity": 50000000
                            },
                            "get_limit": 3,
                            "use_custom_code": false,
                            "bind_openid": false,
                            "can_share": true,
                            "can_give_friend": true,
                            "location_id_list": [123, 12321, 345345],
                            "custom_url_name": "立即使用",
                            "custom_url": "http://www.qq.com",
                            "custom_url_sub_title": "6个汉字tips",
                            "promotion_url_name": "更多优惠",
                            "promotion_url": "http://www.qq.com",
                            "source": "大众点评"   
                        },
                        "deal_detail":  "以下锅底2选1（有菌王锅、麻辣锅、大骨锅、番茄锅、清补凉锅、酸菜鱼锅可选）：\n大锅1份
                            12元\n小锅2份16元"}
                    }
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        data = {
            "card_id": card_id
        }
        url = 'https://api.weixin.qq.com/card/get'
        json_data = self._send_request('post', url, data=data)
        return json_data

    def batchget_card(self, offset, count):
        """Get a list of cards.

        Link:
        https://mp.weixin.qq.com/wiki/3/3f88e06725fd911e6a46e2f5552d80a7.html


        Returns:
            the json data.Example:
            {
                "errcode":0,
                "errmsg":"ok",
                "card_id_list":["ph_gmt7cUVrlRk8swPwx7aDyF-pg"],
                "total_num":1
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        data = {
            "offset": offset,
            "count": count
        }
        url = 'https://api.weixin.qq.com/card/batchget'
        json_data = self._send_request('post', url, data=data)
        return json_data

    def update_card(
        self, card_id, card_type,
        logo_url, notice, description, color, detail=None,
        bonus_cleared=None, bonus_rules=None, balance_rules=None, prerogative=None,
        **infos):
        """Updates a card.

        Link:
        https://mp.weixin.qq.com/wiki/3/3f88e06725fd911e6a46e2f5552d80a7.html

        Returns:
            the json data.Example:
            {
                "errcode":0,
                "errmsg":"ok"
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        base_info = {
            "logo_url": logo_url,
            "notice": notice,
            "description": description,
            "color": color,
            "detail": detail
        }
        base_info.update(infos)
        data = {
            "card_id": card_id,
            card_type.lower(): {
                "base_info": base_info,
                "bonus_cleared": bonus_cleared,
                "bonus_rules": bonus_rules,
                "balance_rules": balance_rules,
                "prerogative": prerogative
            }
        }

        url = 'https://api.weixin.qq.com/card/update'
        json_data = self._send_request('post', url, data=data)
        return json_data

    def modify_stock(
        self, card_id,
        increase_stock_value=None, 
        reduce_stock_value=None):
        """Modifies the stock of a card.

        Link:
        https://mp.weixin.qq.com/wiki/3/3f88e06725fd911e6a46e2f5552d80a7.html

        Returns:
            the json data.Example:
            {
                "errcode":0,
                "errmsg":"ok"
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        data = {
            "card_id": card_id,
        }
        if increase_stock_value:
            data["increase_stock_value"] = increase_stock_value
        if reduce_stock_value:
            data["reduce_stock_value"] = reduce_stock_value

        url = 'https://api.weixin.qq.com/card/modifystock'
        json_data = self._send_request('post', url, data=data)
        return json_data

    def update_code(self, code, new_code, card_id=None):
        """Updates the code.

        Link:
        https://mp.weixin.qq.com/wiki/3/3f88e06725fd911e6a46e2f5552d80a7.html

        Returns:
            the json data.Example:
            {
                "errcode":0,
                "errmsg":"ok"
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        data = {
            "code": code,
            "new_code": new_code
        }
        if card_id:
            data["card_id"] = card_id
        url = 'https://api.weixin.qq.com/card/code/update'
        json_data = self._send_request('post', url, data=data)
        return json_data

    def delete_card(self, card_id):
        """Deletes the card.

        Link:
        https://mp.weixin.qq.com/wiki/3/3f88e06725fd911e6a46e2f5552d80a7.html

        Returns:
            the json data.Example:
            {
                "errcode":0,
                "errmsg":"ok"
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        data = {
            "card_id": card_id
        }
        url = 'https://api.weixin.qq.com/card/delete'
        json_data = self._send_request('post', url, data=data)
        return json_data
