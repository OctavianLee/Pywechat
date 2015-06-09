# -*- coding: utf-8 -*-
from pywechat.services.wechat_shake import ShakeService
from pywechat.services.wechat_card import CardService

from pywechat.excepts import CodeBuildError


class WechatService(object):
    """This class is a role of factory.

    Attributes:
        app_id: the app id of a wechat account.
        app_secret: the app secret of a wechat account.
    """
    def __init__(self, app_id, app_secret):
        """Initializes the class."""
        self.__app_id = app_id
        self.__app_secret = app_secret

    def init_service(self, service_name):
        """Init the service of wechat by service_name.

        Args:
            service_name: the name of wechat's service.

        Returns:
            the service of wechat

        Rasies:
            SystemError
        """
        services = {
            'Shake': ShakeService,
            'Card': CardService
        }

        if not services.has_key(service_name):
            raise CodeBuildError('Service name wrong')
        return services[service_name](self.__app_id, self.__app_secret)
