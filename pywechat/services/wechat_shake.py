# -*- coding: utf-8 -*-
import json

from basic import Basic


class ShakeService(Basic):
    """This class is an implement of the Wechat service of shaking.

    All request's urls come from the official documents.
    Link: https://mp.weixin.qq.com/wiki/home/index.html

    """

    def bind_page(
        self, 
        page_ids, bind, append,
        device_id=None, uuid=None, major=None, minor=None):
        """Binds the relations ship between the device and pages.

        Link:
        https://mp.weixin.qq.com/wiki/12/c8120214ec0ba08af5dfcc0da1a11400.html

        Args:
            page_ids: the list of page_id.
            bind: the mark of binding operation. 
                0 is to dismiss the relationship.
                1 is to build the relationship.
            append: the mark of appending operation.
                0 is to bestrow the page.
                1 is to append the page.
            device_id: the device id, 
                it can be None when UUID, major and minor are seted.
            uuid: the uuid of device.
            major: the major of device.
            minor: the minor of device.

        Returns:
            the json data.Example:
            {
                "data": {
                },
                "errcode": 0,
                "errmsg": "success."
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        data = {
            "page_ids": page_ids,
            "bind": bind,
            "append": append
        }
        if device_id:
            data["device_identifier"] = {
                "device_id": device_id
            }
        else:
            data["device_identifier"] = {
                "uuid": uuid,
                "major": major,
                "minor": minor
            }

        url = 'https://api.weixin.qq.com/shakearound/device/bindpage'
        json_data = self._send_request('post', url, data=data)
        return json_data

    def upload_material(self, image):
        """Uploads the material for the icon of page.

        Formats: jpg, jpeg, png, gif. Size: better 120*120, limit 200*200 px

        Link:
        https://mp.weixin.qq.com/wiki/5/e997428269ff189d8f9a4b9e177be2d9.html

        Args:
            image: the file of image. open(image_name, 'rb')

        Returns:
            the json data.Example:
            {
                "data": {
                    "pic_url":
                    "http://shp.qpic.cn/wechat_shakearound_pic/0/1428377032e9dd2797018cad79186e03e8c5aec8dc/120"
                },
                "errcode": 0,
                "errmsg": "success."
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        url = 'https://api.weixin.qq.com/shakearound/material/add'
        files = {'media': image}
        json_data = self._send_request('post', url, files=files)
        return json_data

    def apply_devices(
        self, 
        quantity, apply_reason, comment, 
        poi_id=None): 
        """Applys devices from the wechat.

        Link:
        https://mp.weixin.qq.com/wiki/15/b9e012f917e3484b7ed02771156411f3.html

        Args:
            quantity: the quantity of devices.(less than 500)
            apply_reason: the reason of applying(less than 100 characters)
            comment: the coment(less than 15 characters or 30 letters)
            poi_id: the id of poin of interest

        Returns:
            the json data.Example:
            {
                "data": {
                    "apply_id": 123,
                    "device_identifiers":[
                        {
                            "device_id":10100,  
                            "uuid":"FDA50693-A4E2-4FB1-AFCF-C6EB07647825",    
                            "major":10001,
                            "minor":10002
                        }
                    ]
                },
                "errcode": 0,
                "errmsg": "success."
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        url = 'https://api.weixin.qq.com/shakearound/device/applyid'
        data = {
            "quantity": quantity,
            "apply_reason": apply_reason,
            "comment": comment
        }
        if poi_id:
            data["poi_id"] = poi_id
        json_data = self._send_request('post', url, data=data)
        return json_data

    def update_device(
        self, 
        comment,
        device_id=None, uuid=None, major=None, minor=None):
        """Edit the comment of a device.

        Link:
        https://mp.weixin.qq.com/wiki/15/b9e012f917e3484b7ed02771156411f3.html

        Args:
            comment: the coment(less than 15 characters or 30 letters)
            device_id: the device id, 
                it can be None when UUID, major and minor are seted.
            uuid: the uuid of device.
            major: the major of device.
            minor: the minor of device.

        Returns:
            the json data.Example:
            {
                "data": {
                },
                "errcode": 0,
                "errmsg": "success."
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        data = {
            "comment": comment,
        }
        if device_id:
            data["device_identifier"] = {
                "device_id": device_id
            }
        else:
            data["device_identifier"] = {
                "uuid": uuid,
                "major": major,
                "minor": minor
            }
        url = 'https://api.weixin.qq.com/shakearound/device/update'
        json_data = self._send_request('post', url, data=data)
        return json_data

    def bind_location(
        self,
        poi_id,
        device_id=None, uuid=None, major=None, minor=None):
        """Bind the device with a location.

        Link:
        https://mp.weixin.qq.com/wiki/15/b9e012f917e3484b7ed02771156411f3.html

        Args:
            poi_id: the id of poin of interest
            device_id: the device id, 
                it can be None when UUID, major and minor are seted.
            uuid: the uuid of device.
            major: the major of device.
            minor: the minor of device.

        Returns:
            the json data.Example:
            {
                "data": {
                },
                "errcode": 0,
                "errmsg": "success."
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        data = {
            "poi_id": poi_id
        }
        if device_id:
            data["device_identifier"] = {
                "device_id": device_id
            }
        else:
            data["device_identifier"] = {
                "uuid": uuid,
                "major": major,
                "minor": minor
            }
        url = 'https://api.weixin.qq.com/shakearound/device/bindlocation'
        json_data = self._send_request('post', url, data=data)
        return json_data

    def search_device(
        self,
        device_id=None, uuid=None, major=None, minor=None):
        """Finds the information of a device.

        Link:
        https://mp.weixin.qq.com/wiki/15/b9e012f917e3484b7ed02771156411f3.html

        Args:
            device_id: the device id, 
                it can be None when UUID, major and minor are seted.
            uuid: the uuid of device.
            major: the major of device.
            minor: the minor of device.

        Returns:
            the json data.Example:
            {
                "data": {
                    "devices": [
                        {
                          "comment": "",
                          "device_id": 10097,
                          "major": 10001,
                          "minor": 12102,
                          "page_ids": "15369",
                          "status": 1,
                          "poi_id": 0,
                          "uuid": "FDA50693-A4E2-4FB1-AFCF-C6EB07647825"
                        }
                    ],
                    "total_count": 1
                },
                "errcode": 0,
                "errmsg": "success."
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        device_identifier = {} 
        if device_id:
            device_identifier = {
                "device_id": device_id
            }
        else:
            device_identifier = {
                "uuid": uuid,
                "major": major,
                "minor": minor
            }
        data = {
            "device_identifiers": [device_identifier]
        }
        url = 'https://api.weixin.qq.com/shakearound/device/search'
        json_data = self._send_request('post', url, data=data)
        return json_data

    def search_devices(
        self, 
        begin, count,
        apply_id=None):
        """Finds the information of devices.

        Link:
        https://mp.weixin.qq.com/wiki/15/b9e012f917e3484b7ed02771156411f3.html

        Args:
            begin: the start number of devices.
            count: the number of devices will query.
            apply_id: the applicaition number of devices.

        Returns:
            the json data.Example:
            {
                "data": {
                    "devices": [
                        {
                          "comment": "",
                          "device_id": 10097,
                          "major": 10001,
                          "minor": 12102,
                          "page_ids": "15369",
                          "status": 1,
                          "poi_id": 0,
                          "uuid": "FDA50693-A4E2-4FB1-AFCF-C6EB07647825"
                        }
                    ],
                    "total_count": 1
                },
                "errcode": 0,
                "errmsg": "success."
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        data = {
            "begin": begin,
            "count": count
        }
        if apply_id:
            data["apply_id"] =  apply_id
        url = 'https://api.weixin.qq.com/shakearound/device/search'
        json_data = self._send_request('post', url, data=data)
        return json_data

    def add_page(
        self,
        title, description, page_url, icon_url,
        comment=None):
        """Adds the new page.

        Link:
        https://mp.weixin.qq.com/wiki/5/6626199ea8757c752046d8e46cf13251.html

        Args:
            title: the page title(less than 6 characters).
            description: the vice title(less than 7 characters).
            page_url: the url of page.
            icon_url: the url of icon.
            comment: the coment(less than 15 characters)

        Returns:
            the json data.Example:
            {
                "data": {
                    "page_id": 28840
                },
                "errcode": 0,
                "errmsg": "success."
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        data = {
            "title": title,
            "description": description,
            "page_url": page_url,
            "icon_url": icon_url
        }
        if comment:
            data["comment"] = comment
        url = 'https://api.weixin.qq.com/shakearound/page/add'
        json_data = self._send_request('post', url, data=data)
        return json_data

    def update_page(
        self, 
        page_id, title, description, page_url, icon_url,
        comment=None):
        """Edits a page.

        Link:
        https://mp.weixin.qq.com/wiki/5/6626199ea8757c752046d8e46cf13251.html

        Args:
            page_id: the id of page.
            title: the page title(less than 6 characters).
            description: the vice title(less than 7 characters).
            page_url: the url of page.
            icon_url: the url of icon.
            comment: the coment(less than 15 characters)

        Returns:
            the json data.Example:
            {
                "data": {
                    "page_id": 28840
                },
                "errcode": 0,
                "errmsg": "success."
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        data = {
            "page_id": page_id,
            "title": title,
            "description": description,
            "page_url": page_url,
            "icon_url": icon_url
        }
        if comment:
            data["comment"] = comment
        url = 'https://api.weixin.qq.com/shakearound/page/update'
        json_data = self._send_request('post', url, data=data)
        return json_data

    def search_page_by_ids(self, page_ids):
        """Finds pages by ids.

        Link:
        https://mp.weixin.qq.com/wiki/5/6626199ea8757c752046d8e46cf13251.html

        Args:
            page_ids: the list of page id.

        Returns:
            the json data.Example:
            {
                "data": {
                    "pages": [
                        {
                            "comment": "just for test",
                            "description": "test",
                            "icon_url": "https://www.baidu.com/img/bd_logo1",
                            "page_id": 28840,
                            "page_url": "http://xw.qq.com/testapi1",
                            "title": "测试1"
                        }
                    ],
                    "total_count": 1
                },
                "errcode": 0,
                "errmsg": "success."
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        data = {
            "page_ids": page_ids,
        }
        url = 'https://api.weixin.qq.com/shakearound/page/search'
        json_data = self._send_request('post', url, data=data)
        return json_data

    def search_page_by_counts(self, begin, count):
        """Finds pages by counts.

        Link:
        https://mp.weixin.qq.com/wiki/5/6626199ea8757c752046d8e46cf13251.html

        Args:
            begin: the start number of pages.
            count: the number of pages will query.

        Returns:
            the json data.Example:
            {
                "data": {
                    "pages": [
                        {
                            "comment": "just for test",
                            "description": "test",
                            "icon_url": "https://www.baidu.com/img/bd_logo1",
                            "page_id": 28840,
                            "page_url": "http://xw.qq.com/testapi1",
                            "title": "测试1"
                        }
                    ],
                    "total_count": 1
                },
                "errcode": 0,
                "errmsg": "success."
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        data = {
            "begin": begin,
            "count": count
        }
        url = 'https://api.weixin.qq.com/shakearound/page/search'
        json_data = self._send_request('post', url, data=data)
        return json_data

    def delete_page(self, page_ids):
        """Deletes pages by ids.

        Link:
        https://mp.weixin.qq.com/wiki/5/6626199ea8757c752046d8e46cf13251.html

        Args:
            page_ids: the list of page id.

        Returns:
            the json data.Example:
            {
                "data": {
                },
                "errcode": 0,
                "errmsg": "success."
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        data = {
            "page_ids": page_ids,
        }
        url = 'https://api.weixin.qq.com/shakearound/page/delete'
        json_data = self._send_request('post', url, data=data)
        return json_data

    def get_shake_info(self, ticket, need_poi=None, access_token=None):
        """Gets the informaiton of shaking.

        Gets the information of devices including UUID, major, minor etc.

        Link:
        https://mp.weixin.qq.com/wiki/3/34904a5db3d0ec7bb5306335b8da1faf.html

        Args:
            ticket: the ticket of business which can be getted from url.
            need_poi: whether it needs to return poi_id. 
                1 is to return.

        Returns:
            the json data.Example:
            {
                "data": {
                },
                "errcode": 0,
                "errmsg": "success."
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        data = {
            "ticket": ticket
        }
        if need_poi:
            data["need_poi"] = need_poi
        url = 'https://api.weixin.qq.com/shakearound/user/getshakeinfo'
        json_data = self._send_request('post', url, data=data)
        return json_data

    def device_statistics(
        self, 
        begin_date, end_date,
        device_id=None, uuid=None, major=None, minor=None):
        """Gets the statistics of a device.

        Link:
        https://mp.weixin.qq.com/wiki/0/8a24bcacad40fe7ee98d1573cb8a6764.html

        Args:
            begin_date: the timestamp of start date 
            end_date: the timestamp of end date, the max time span is 30 days.
            device_id: the device id, 
                it can be None when UUID, major and minor are seted.
            uuid: the uuid of device.
            major: the major of device.
            minor: the minor of device.

        Returns:
            the json data.Example:
            {
                "data": [
                    {
                        "click_pv": 0,
                        "click_uv": 0,
                        "ftime": 1425052800,
                        "shake_pv": 0,
                        "shake_uv": 0
                    }
                ],
                
                "errcode": 0,
                "errmsg": "success."
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        data = {
            "begin_date": begin_date,
            "end_date": end_date
        }
        if device_id:
            data["device_identifier"] = {
                "device_id": device_id
            }
        else:
            data["device_identifier"] = {
                "uuid": uuid,
                "major": major,
                "minor": minor
            }
        url = 'https://api.weixin.qq.com/shakearound/statistics/device'
        json_data = self._send_request('post', url, data=data)
        return json_data

    def page_statistics(self, page_id, begin_date, end_date):
        """Finds the information of a page.

        (Link:
        https://mp.weixin.qq.com/wiki/0/8a24bcacad40fe7ee98d1573cb8a6764.html)

        Args:
            begin_date: the timestamp of start date 
            end_date: the timestamp of end date, the max time span is 30 days.
            page_id: the id of page.

        Returns:
            the json data.Example:
            {
                "data": [
                    {
                        "click_pv": 0,
                        "click_uv": 0,
                        "ftime": 1425052800,
                        "shake_pv": 0,
                        "shake_uv": 0
                    }
                ],
                
                "errcode": 0,
                "errmsg": "success."
            }

        Raises:
            WechatError: to raise the exception if it contains the error.
        """

        data = {
            "page_id": page_id,
            "begin_date": begin_date,
            "end_date": end_date
        }
        url = 'https://api.weixin.qq.com/shakearound/statistics/page'
        json_data = self._send_request('post', url, data=data)
        return json_data
