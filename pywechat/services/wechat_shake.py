# -*- coding: utf-8 -*-
import json
import requests

from basic import Basic

class ShakeService(Basic):
    """This class is an implement of the Wechat service of shaking.


    All request's urls come from the official documents.
    (Link: https://mp.weixin.qq.com/wiki/home/index.html)
    """

    def bind_the_page(
        self, page_ids, bind, append,
        device_id=None, uuid=None, major=None, minor=None):
        """Binds the relations ship between the device and pages.

        (Link:
        https://mp.weixin.qq.com/wiki/12/c8120214ec0ba08af5dfcc0da1a11400.html)

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
            json_data: the json data of the returns.
        """
        device_identifier = None
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
            "device_identifier": device_identifier,
            "page_ids": page_ids,
            "bind": bind,
            "append": append
        }
        data = json.dumps(data)

        url = 'https://api.weixin.qq.com/shakearound/device/bindpage?'
        url += 'access_token={0}'.format(self._get_access_token())
        json_data = requests.post(url, data=data).json()
        return json_data

    def upload_picture(self, image):
        """Uploads the picutre for the icon of page.

        (Link:
        https://mp.weixin.qq.com/wiki/5/e997428269ff189d8f9a4b9e177be2d9.html)

        Args:
            image: the file of image. open(image_name, 'rb')

        Returns:
            json_data: the json data of the returns.
        """
        url = 'https://api.weixin.qq.com/shakearound/material/add?'
        url += 'access_token={0}'.format(self._get_access_token())
        files = {'media': image}
        json_data = requests.post(url, files=files).json()
        return json_data

    def apply_devices(
        self, quantity, apply_reason, comment, 
        poi_id=None): 
        """Applys devices from the wechat.

        (Link:
        https://mp.weixin.qq.com/wiki/15/b9e012f917e3484b7ed02771156411f3.html)

        Args:
            quantity: the quantity of devices.(less than 500)
            apply_reason: the reason of applying(less than 100 characters)
            comment: the coment(less than 15 characters or 30 letters)
            poi_id: the id of poin of interest

        Returns:
            json_data: the json data of the returns.
        """
        url = 'https://api.weixin.qq.com/shakearound/device/applyid?'
        url += 'access_token={0}'.format(self._get_access_token())
        data = {
            "quantity": quantity,
            "apply_reason": apply_reason,
            "comment": comment
        }
        if poi_id:
            data.update({"poi_id": poi_id})
        data = json.dumps(data)
        json_data = requests.post(url, data=data).json()
        return json_data

    def edit_device_info(
        self, comment,
        device_id=None, uuid=None, major=None, minor=None):
        """Edit the comment of a device.

        (Link:
        https://mp.weixin.qq.com/wiki/15/b9e012f917e3484b7ed02771156411f3.html)

        Args:
            comment: the coment(less than 15 characters or 30 letters)
            device_id: the device id, 
                it can be None when UUID, major and minor are seted.
            uuid: the uuid of device.
            major: the major of device.
            minor: the minor of device.

        Returns:
            json_data: the json data of the returns.
        """

        device_identifier = None
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
            "device_identifier": device_identifier,
            "comment": comment,
        }
        data = json.dumps(data)
        url = 'https://api.weixin.qq.com/shakearound/device/update?'
        url += 'access_token={0}'.format(self._get_access_token())
        json_data = requests.post(url, data=data).json()
        return json_data

    def bind_location(
        self, poi_id,
        device_id=None, uuid=None, major=None, minor=None):
        """Bind the device with a location.

        (Link:
        https://mp.weixin.qq.com/wiki/15/b9e012f917e3484b7ed02771156411f3.html)

        Args:
            poi_id: the id of poin of interest
            device_id: the device id, 
                it can be None when UUID, major and minor are seted.
            uuid: the uuid of device.
            major: the major of device.
            minor: the minor of device.

        Returns:
            json_data: the json data of the returns.
        """

        device_identifier = None
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
            "device_identifier": device_identifier,
            "poi_id": poi_id,
        }
        data = json.dumps(data)
        url = 'https://api.weixin.qq.com/shakearound/device/bindlocation?'
        url += 'access_token={0}'.format(self._get_access_token())
        json_data = requests.post(url, data=data).json()
        return json_data

    def find_a_device(
        self,
        device_id=None, uuid=None, major=None, minor=None):
        """Finds the information of a device.

        (Link:
        https://mp.weixin.qq.com/wiki/15/b9e012f917e3484b7ed02771156411f3.html)

        Args:
            device_id: the device id, 
                it can be None when UUID, major and minor are seted.
            uuid: the uuid of device.
            major: the major of device.
            minor: the minor of device.

        Returns:
            json_data: the json data of the returns.
        """
        device_identifier = None
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
            "device_identifier": [device_identifier]
        }
        data = json.dumps(data)
        url = 'https://api.weixin.qq.com/shakearound/device/search?'
        url += 'access_token={0}'.format(self._get_access_token())
        json_data = requests.post(url, data=data).json()
        return json_data

    def find_devices(
        self, begin, count,
        apply_id=None):
        """Finds the information of a device.

        (Link:
        https://mp.weixin.qq.com/wiki/15/b9e012f917e3484b7ed02771156411f3.html)

        Args:
            begin: the start number of devices.
            count: the number of devices will query.
            apply_id: the applicaition number of devices.

        Returns:
            json_data: the json data of the returns.
        """
        data = {
            "begin": begin,
            "count": count
        }
        if apply_id:
            data.update({"apply_id": apply_id})
        data = json.dumps(data)
        url = 'https://api.weixin.qq.com/shakearound/device/search?'
        url += 'access_token={0}'.format(self._get_access_token())
        json_data = requests.post(url, data=data).json()
        return json_data

    def add_new_page(
        self, title, description, page_url, icon_url,
        comment=None):
        """Adds the new page.

        (Link:
        https://mp.weixin.qq.com/wiki/5/6626199ea8757c752046d8e46cf13251.html)

        Args:
            title: the page title(less than 6 characters).
            description: the vice title(less than 7 characters).
            page_url: the url of page.
            icon_url: the url of icon.
            comment: the coment(less than 15 characters)

        Returns:
            json_data: the json data of the returns.
        """
        data = {
            "title": title,
            "description": description,
            "page_url": page_url,
            "icon_url": icon_url
        }
        if comment:
            data.update({"comment": comment})
        data = json.dumps(data)
        url = 'https://api.weixin.qq.com/shakearound/page/add?'
        url += 'access_token={0}'.format(self._get_access_token())
        json_data = requests.post(url, data=data).json()
        return json_data

    def edit_page(
        self, page_id, title, description, page_url, icon_url,
        comment=None):
        """Edits a page.

        (Link:
        https://mp.weixin.qq.com/wiki/5/6626199ea8757c752046d8e46cf13251.html)

        Args:
            page_id: the id of page.
            title: the page title(less than 6 characters).
            description: the vice title(less than 7 characters).
            page_url: the url of page.
            icon_url: the url of icon.
            comment: the coment(less than 15 characters)

        Returns:
            json_data: the json data of the returns.
        """
        data = {
            "page_id": page_id,
            "title": title,
            "description": description,
            "page_url": page_url,
            "icon_url": icon_url
        }
        if comment:
            data.update({"comment": comment})
        data = json.dumps(data)
        url = 'https://api.weixin.qq.com/shakearound/page/update?'
        url += 'access_token={0}'.format(self._get_access_token())
        json_data = requests.post(url, data=data).json()
        return json_data

    def find_pages_by_ids(self, page_ids):
        """Finds pages by ids.

        (Link:
        https://mp.weixin.qq.com/wiki/5/6626199ea8757c752046d8e46cf13251.html)

        Args:
            page_ids: the list of page id.

        Returns:
            json_data: the json data of the returns.
        """
        data = {
            "page_ids": page_ids,
        }
        data = json.dumps(data)
        url = 'https://api.weixin.qq.com/shakearound/page/search?'
        url += 'access_token={0}'.format(self._get_access_token())
        json_data = requests.post(url, data=data).json()
        return json_data

    def find_pages_by_counts(self, begin, count):
        """Finds pages by counts.

        (Link:
        https://mp.weixin.qq.com/wiki/5/6626199ea8757c752046d8e46cf13251.html)

        Args:
            begin: the start number of pages.
            count: the number of pages will query.

        Returns:
            json_data: the json data of the returns.
        """
        data = {
            "begin": begin,
            "count": count
        }
        data = json.dumps(data)
        url = 'https://api.weixin.qq.com/shakearound/page/search?'
        url += 'access_token={0}'.format(self._get_access_token())
        json_data = requests.post(url, data=data).json()
        return json_data

    def delete_pages_by_ids(self, page_ids):
        """Deletes pages by ids.

        (Link:
        https://mp.weixin.qq.com/wiki/5/6626199ea8757c752046d8e46cf13251.html)

        Args:
            page_ids: the list of page id.

        Returns:
            json_data: the json data of the returns.
        """
        data = {
            "page_ids": page_ids,
        }
        data = json.dumps(data)
        url = 'https://api.weixin.qq.com/shakearound/page/delete?'
        url += 'access_token={0}'.format(self._get_access_token())
        json_data = requests.post(url, data=data).json()
        return json_data

    def get_shake_info(self, ticket, need_poi=None):
        """Gets the informaiton of shaking.

        Gets the information of devices including UUID, major, minor etc.

        (Link:
        https://mp.weixin.qq.com/wiki/3/34904a5db3d0ec7bb5306335b8da1faf.html)

        Args:
            ticket: the ticket of business which can be getted from url.
            need_poi: whether it needs to return poi_id. 
                1 is to return.

        Returns:
            json_data: the json data of the returns.
        """
        data = {
            "ticket": ticket
        }
        if need_poi:
            data.update({"need_poi": need_poi})
        data = json.dumps(data)
        url = 'https://api.weixin.qq.com/shakearound/user/getshakeinfo?'
        url += 'access_token={0}'.format(self._get_access_token())
        json_data = requests.post(url, data=data).json()
        return json_data

    def get_statistics_for_device(
        self, begin_date, end_date,
        device_id=None, uuid=None, major=None, minor=None):
        """Finds the information of a device.

        (Link:
        https://mp.weixin.qq.com/wiki/0/8a24bcacad40fe7ee98d1573cb8a6764.html)

        Args:
            begin_date: the timestamp of start date 
            end_date: the timestamp of end date, the max time span is 30 days.
            device_id: the device id, 
                it can be None when UUID, major and minor are seted.
            uuid: the uuid of device.
            major: the major of device.
            minor: the minor of device.

        Returns:
            json_data: the json data of the returns.
        """
        device_identifier = None
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
            "device_identifier": device_identifier,
            "begin_date": begin_date,
            "end_date": end_date
        }
        data = json.dumps(data)
        url = 'https://api.weixin.qq.com/shakearound/'
        url += 'statistics/device?'
        url += 'access_token={0}'.format(self._get_access_token())
        json_data = requests.post(url, data=data).json()
        return json_data

    def get_statistics_for_page(self, page_id, begin_date, end_date):
        """Finds the information of a page.

        (Link:
        https://mp.weixin.qq.com/wiki/0/8a24bcacad40fe7ee98d1573cb8a6764.html)

        Args:
            begin_date: the timestamp of start date 
            end_date: the timestamp of end date, the max time span is 30 days.
            page_id: the id of page.

        Returns:
            json_data: the json data of the returns.
        """
        data = {
            "page_id": page_id,
            "begin_date": begin_date,
            "end_date": end_date
        }
        data = json.dumps(data)
        url = 'https://api.weixin.qq.com/shakearound/'
        url += 'statistics/page?'
        url += 'access_token={0}'.format(self._get_access_token())
        json_data = requests.post(url, data=data).json()
        return json_data

