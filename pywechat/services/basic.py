# -*- coding: utf-8 -*-
import requests


class Basic(object):
    """The basic class of all services.
    """
    def __init__(self, app_id, app_secret):
        """Initializes the service.

        Args:
            app_id: the app id of a wechat account.
            app_secret: the app secret of a wechat account.
        """
        self.__app_id = app_id
        self.__app_secret = app_secret
    
    def _get_access_token(self):
        """Gets the access token from wechat.

        (Link:
        https://mp.weixin.qq.com/wiki/11/0e4b294685f817b95cbed85ba5e82b8f.html)

        Returns:
            access_token: the access token requests from the wechat.
        """

        #Checks whether the access token is in memcache,
        url = 'https://api.weixin.qq.com/cgi-bin/token?'
        url += 'grant_type=client_credential&'
        url += 'appid={0}&secret={1}'.format(
            self.__app_id,
            self.__app_secret)
        token_json = requests.get(url, verify=True).json()
        access_token = token_json.get('access_token')
        expires_in = token_json.get('expires_in')
        return access_token, expires_in