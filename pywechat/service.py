# -*- coding: utf-8 -*-
from services.wechat_shake import ShakeService


class WechatService(object):
    """This class is a role of factory.
    """

    @staticmethod
    def init_service(app_id, app_secret, service_name, flag=None):
        """Init the service of wechat by service_name

        Args:
            service_name: the name of wechat's service.
            app_id: the app id of a wechat account.
            app_secret: the app secret of a wechat account.
            flag: the mark for memcached's key.(String)

        Returns:
            the service of wechat
        """
        services = {
            'Shake': ShakeService
        }
        if not services.has_key(service_name):
            raise NameError
        return services[service_name](app_id, app_secret, flag)


