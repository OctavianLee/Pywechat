# -*- coding: utf-8 -*-
import json
import requests

from basic import Basic

class CardService(Basic):
    """This class is an implement of the Wechat service of card.


    All request's urls come from the official documents.
    (Link: https://mp.weixin.qq.com/wiki/home/index.html)
    """

    def upload_image(self, image):
        """Uploads the image for the logo of card.

        (Link:
        https://mp.weixin.qq.com/wiki/8/b7e310e7943f7763450eced91fa793b0.html)

        Args:
            image: the file of image. open(image_name, 'rb')

        Returns:
            json_data: the json data of the returns.
        """
        url = 'https://api.weixin.qq.com/cgi-bin/media/uploadimg?'
        url += 'access_token={0}'.format(self._get_access_token())
        files = {'buffer': image}
        json_data = requests.post(url, files=files).json()
        return json_data
        
    def get_colors(self):
        """Gets the available colors of cards.

        (Link:
        https://mp.weixin.qq.com/wiki/8/b7e310e7943f7763450eced91fa793b0.html)

        Returns:
            json_data: the json data of the returns.
        """
        url = 'https://api.weixin.qq.com/card/getcolors?'
        url += 'access_token={0}'.format(self._get_access_token())
        json_data = requests.post(url).json()
        return json_data

    def create_card(
        self, card_dict,
        logo_url, code_type, brand_name, title,
        color, notice, description, quantity, type,
        **infos):
        """Creates a card.

        (Link:
        https://mp.weixin.qq.com/wiki/8/b7e310e7943f7763450eced91fa793b0.html)

        Returns:
            json_data: the json data of the returns."""
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
          "groupon": {
              base_info
          }
        }
        data.update(card_dict)
        data = json.dumps(data)

        url = 'https://api.weixin.qq.com/card/create?'
        url += 'access_token={0}'.format(self._get_access_token())
        json_data = requests.post(url, data=data).json()
        return json_data



        




