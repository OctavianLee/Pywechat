# -*- coding: utf-8 -*-
import json
import requests

from basic import Basic

class CardService(Basic):
    """This class is an implement of the Wechat service of card.


    All request's urls come from the official documents.
    (Link: https://mp.weixin.qq.com/wiki/home/index.html)
    """

    def upload_image(self, image, access_token=None):
        """Uploads the image for the logo of card.

        (Link:
        https://mp.weixin.qq.com/wiki/8/b7e310e7943f7763450eced91fa793b0.html)

        Args:
            image: the file of image. open(image_name, 'rb')

        Returns:
            json_data: the json data of the returns.
        """
        if not access_token:
            access_token, expire_in = self._get_access_token()
        url = 'https://api.weixin.qq.com/cgi-bin/media/uploadimg?'
        url += 'access_token={0}'.format(access_token)
        files = {'buffer': image}
        json_data = requests.post(url, files=files).json()
        return json_data
        
    def get_colors(self, access_token=None):
        """Gets the available colors of cards.

        (Link:
        https://mp.weixin.qq.com/wiki/8/b7e310e7943f7763450eced91fa793b0.html)

        Returns:
            json_data: the json data of the returns.
        """
        if not access_token:
            access_token, expire_in = self._get_access_token()
        url = 'https://api.weixin.qq.com/card/getcolors?'
        url += 'access_token={0}'.format(access_token)
        json_data = requests.post(url).json()
        return json_data

    def create_card(
        self, card_dict, card_type,
        logo_url, code_type, brand_name, title,
        color, notice, description, quantity, type,
        access_token=None,
        **infos):
        """Creates a card.

        (Link:
        https://mp.weixin.qq.com/wiki/8/b7e310e7943f7763450eced91fa793b0.html)

        Returns:
            json_data: the json data of the returns."""
        if not access_token:
            access_token, expire_in = self._get_access_token()
        info_dict = {name: value for name, value in infos}
        date_info = None
        if (info_dict.has_key('begin_timestamp') and 
            info_dict.has_key('end_timestamp')):
            date_info = {
              "type": type,
              "begin_timestamp": info_dict['begin_timestamp'],
              "end_timestamp": info_dict['end_timestamp']
            }
            del info_dict['begin_timestamp']
            del info_dict['end_timestamp']
        else:
            date_info = {
              "type": type,
            }

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
        }
        base_info.update(date_info)
        base_info.update(info_dict)
        data = {
          card_type: {
              base_info
          }
        }
        data.update(card_dict)
        data = json.dumps(data)

        url = 'https://api.weixin.qq.com/card/create?'
        url += 'access_token={0}'.format(access_token)
        json_data = requests.post(url, data=data).json()
        return json_data

    def create_qrcode(
        self,
        code, access_token=None, **args):
        """Creates a qr code.

        (Link:
        https://mp.weixin.qq.com/wiki/12/ccd3aa0bddfe5211aace864de00b42e0.html)

        Returns:
            json_data: the json data of the returns.
        """
        if args:
            info_dict = {name: value for name, value in args}
        if access_token:
            access_token, expire_in = self._get_access_token()

        data = {
            "action_name": "QR_CARD",
            "action_info": {
                "card": {
                    info_dict
                }
            }
        }
        data = json.dumps(data)

        url = 'https://api.weixin.qq.com/card/qrcode/create?'
        url += 'access_token={0}'.format(access_token)
        json_data = requests.post(url, data=data).json()
        return json_data

    def check_code(
        self, 
        code, card_id=None, access_token=None):
        """Check the code is available.

        (Link:
        https://mp.weixin.qq.com/wiki/12/ccd3aa0bddfe5211aace864de00b42e0.html)

        Returns:
            json_data: the json data of the returns.
        """
        data = {
            "code": code
        }
        if card_id:
            data.update({"card_id": card_id})
        data = json.dumps(data)
        if access_token:
            access_token, expire_in = self._get_access_token()

        url = 'https://api.weixin.qq.com/card/code/unavailable?'
        url += 'access_token={0}'.format(access_token)
        json_data = requests.post(url, data=data).json()
        return json_data

    def decrypt_code(
        self,
        encrypt_code, access_token=None):
        """decrypt the code.

        (Link:
        https://mp.weixin.qq.com/wiki/12/ccd3aa0bddfe5211aace864de00b42e0.html)

        Returns:
            json_data: the json data of the returns.
        """
        if access_token:
            access_token, expire_in = self._get_access_token()
        data = {
            "encrypt_code": encrypt_code
        }
        data = json.dumps(data)
        url = 'https://api.weixin.qq.com/card/code/decrtpt?'
        url += 'access_token={0}'.format(access_token)
        json_data = requests.post(url, data=data).json()
        return json_data

    def get_code(
        self, 
        code, card_id=None, access_token=None):
        """Get the code.

        (Link:
        https://mp.weixin.qq.com/wiki/3/3f88e06725fd911e6a46e2f5552d80a7.html)

        Returns:
            json_data: the json data of the returns.
        """
        data = {
            "code": code
        }
        if card_id:
            data.update({"card_id": card_id})
        data = json.dumps(data)
        if access_token:
            access_token, expire_in = self._get_access_token()

        url = 'https://api.weixin.qq.com/card/code/get?'
        url += 'access_token={0}'.format(access_token)
        json_data = requests.post(url, data=data).json()
        return json_data

    def get_card(
        self, 
        card_id, access_token=None):
        """Get the card.

        (Link:
        https://mp.weixin.qq.com/wiki/3/3f88e06725fd911e6a46e2f5552d80a7.html)

        Returns:
            json_data: the json data of the returns.
        """
        data = {
            "card_id": card_id
        }
        data = json.dumps(data)
        if access_token:
            access_token, expire_in = self._get_access_token()

        url = 'https://api.weixin.qq.com/card/get?'
        url += 'access_token={0}'.format(access_token)
        json_data = requests.post(url, data=data).json()
        return json_data

    def batchget_card(
        self, 
        offset, count, access_token=None):
        """Get a list of cards.

        (Link:
        https://mp.weixin.qq.com/wiki/3/3f88e06725fd911e6a46e2f5552d80a7.html)

        Returns:
            json_data: the json data of the returns.
        """
        data = {
            "offset": offset,
            "count": count
        }
        data = json.dumps(data)
        if access_token:
            access_token, expire_in = self._get_access_token()

        url = 'https://api.weixin.qq.com/card/batchget?'
        url += 'access_token={0}'.format(access_token)
        json_data = requests.post(url, data=data).json()
        return json_data

    def update_card(
        self, card_id, card_type,
        logo_url, notice, description, color, detail,
        bonus_cleared, bonus_rules, balance_rules, prerogative,
        access_token=None,
        **infos):
        """Updates a card.

        (Link:
        https://mp.weixin.qq.com/wiki/3/3f88e06725fd911e6a46e2f5552d80a7.html)

        Returns:
            json_data: the json data of the returns."""
        if not access_token:
            access_token, expire_in = self._get_access_token()
        info_dict = {name: value for name, value in infos}

        base_info = {
            "logo_url": logo_url,
            "notice": notice,
            "description": description,
            "color": color,
            "detail": detail
        }
        base_info.update(info_dict)
        data = {
            "card_id": card_id,
            card_type: {
                "base_info": base_info,
                "bonus_cleared": bonus_cleared,
                "bonus_rules": bonus_rules,
                "prerogative": prerogative
            }
        }
        data = json.dumps(data)

        url = 'https://api.weixin.qq.com/card/update?'
        url += 'access_token={0}'.format(access_token)
        json_data = requests.post(url, data=data).json()
        return json_data

    def modify_stock(
        self, 
        increase_stock_value=None, reduce_stock_value=None,
        access_token=None):
        """Modifies the stock of a card.

        (Link:
        https://mp.weixin.qq.com/wiki/3/3f88e06725fd911e6a46e2f5552d80a7.html)

        Returns:
            json_data: the json data of the returns."""
        if not access_token:
            access_token, expire_in = self._get_access_token()
        data = {
            "card_id": card_id,
        }
        if increase_stock_value:
            data.update({"increase_stock_value": increase_stock_value})
        if reduce_stock_value:
            data.update({"reduce_stock_value": reduce_stock_value})
        data = json.dumps(data)

        url = 'https://api.weixin.qq.com/card/modifystock?'
        url += 'access_token={0}'.format(access_token)
        json_data = requests.post(url, data=data).json()
        return json_data

    def update_code(
        self,
        code, new_code, card_id=None, access_token=None):
        """Updates the code.

        (Link:
        https://mp.weixin.qq.com/wiki/3/3f88e06725fd911e6a46e2f5552d80a7.html)

        Returns:
            json_data: the json data of the returns."""
        if not access_token:
            access_token, expire_in = self._get_access_token()
        data = {
            "code": code,
            "new_code": new_code
        }
        if card_id:
            data.update({"card_id": card_id})
        data = json.dumps(data)
        if access_token:
            access_token, expire_in = self._get_access_token()

        url = 'https://api.weixin.qq.com/card/code/update?'
        url += 'access_token={0}'.format(access_token)
        json_data = requests.post(url, data=data).json()
        return json_data

    def delete_card(
        self,
        card_id, access_token=None):
        """Updates the code.

        (Link:
        https://mp.weixin.qq.com/wiki/3/3f88e06725fd911e6a46e2f5552d80a7.html)

        Returns:
            json_data: the json data of the returns."""
        if not access_token:
            access_token, expire_in = self._get_access_token()
        data = {
            "card_id": card_id
        }
        data = json.dumps(data)
        url = 'https://api.weixin.qq.com/card/delete?'
        url += 'access_token={0}'.format(access_token)
        json_data = requests.post(url, data=data).json()
        return json_data

    def set_unavailable(
        self, code, card_id=None, access_token=None):
        """Sets a card status Unavialble.

        (Link:
        https://mp.weixin.qq.com/wiki/3/3f88e06725fd911e6a46e2f5552d80a7.html)

        Returns:
            json_data: the json data of the returns."""
        return self.check_code(code, card_id, access_token)
