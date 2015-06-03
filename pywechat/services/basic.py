# -*- coding: utf-8 -*-
import json
import time
import requests

from pywechat.excepts import WechatError


class Basic(object):
    """The basic class of all services.

    Attributes:
        app_id: the app id of a wechat account.
        app_secret: the app secret of a wechat account.
        access_token: the access token requests from the wechat.
        token_expires_time: the time that the access token will expire.
    """
    
    def __init__(self, app_id, app_secret):
        """Initializes the service."""
        self.__app_id = app_id
        self.__app_secret = app_secret
        self.__access_token = self._grant_access_token()
        self.__token_expires_time = None
    
    @property
    def access_token(self):
        #check the access token
        if self.__access_token and (self.__token_expires_time > time.time()):
            return self.__access_token

        #if access token is invaild, grant it.
        self._grant_access_token()
        return self.__access_token

    def _send_request(self, method, url, **kwargs):
        """Send a request to the server.

        Args:
            method: the method of request.('get', 'post', etc)
            url: the request's url.
            kwargs: the data will send to.

        Returns:
            the json data gets from the server.

        Raises:
            WechatError: to raise the exception if it contains the error.
        """
        if not kwargs.get('params'):
            kwargs['params'] = {
                "access_token": self.access_token
            }
        if kwargs.get('data'):
            data = json.dumps(kwargs['data']).encode('utf8')
            kwargs["data"] = data

        try:
            r = requests.request(
                method=method,
                url=url,
                **kwargs
            )
        except Exception as e:
            print e

        r.raise_for_status()
        json_data = r.json()
        self._check_wechat_error(json_data)
        return json_data

    def _check_wechat_error(self, json_data):
        """Check whether the data from the plaform of wechat is an error.

        Args:
            json_data: the json data gained from the wechat.

        Raises:
            WechatError: to raise the exception if it contains the error.
        """
        errcode = json_data.get('errcode')
        if errcode and errcode != 0:
            raise WechatError(errcode, json_data.get('errmsg'))

    def _grant_access_token(self):
        """Gets the access token from wechat.

        Public account can use this method with APPID and APPSecret to gain
        the access token.

        Link:
        https://mp.weixin.qq.com/wiki/11/0e4b294685f817b95cbed85ba5e82b8f.html

        Returns:
            the json data.Example:
            {"access_token":"ACCESS_TOKEN","expires_in":7200}

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        #Checks whether the access token is in memcache,
        url = 'https://api.weixin.qq.com/cgi-bin/token'
        params = {
            "grant_type": "client_credential",
            "appid": self.__app_id,
            "secret": self.__app_secret
        }
        json_data = self._send_request('get', url, params=params)
        self.__access_token = json_data.get('access_token')
        self.__token_expires_time = time.time() + json_data.get('expires_in')
        return json_data

    def _get_wechat_server_ips(self):
        """Gets the ip list from wechat.

        For the reason of security, it needs the list of ip addresses of wechat
        to limit some conditions.

        Link:
        https://mp.weixin.qq.com/wiki/0/2ad4b6bfd29f30f71d39616c2a0fcedc.html

        Returns:
            the json data.Example:
            {
                "ip_list":["127.0.0.1","127.0.0.1"]
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """
        url = "https://api.weixin.qq.com/cgi-bin/getcallbackip"
        params = {
            "access_token": self.access_token
        }
        json_data = self._send_request('get', url, params=params)
        return json_data
