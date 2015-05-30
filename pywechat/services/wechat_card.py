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

