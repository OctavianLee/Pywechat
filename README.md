# Pywechat
Encapsulates wechat's APIs with Python.
微信公众平台api

If you wants to fix the code or help me complete the whole project, just send me
the pull request!

## Todo

+ Impove codes
+ Add the service of card
+ Add some exceptions
+ Test interfaces


## How to use

Libs:

+ requests

``` shell
pip install -r requirements.txt
```

Then you can use the Service.

``` python
from pywechat import WechatService

app_id = 'XXX'
app_secret = 'XXX'
service = WechatService(app_id, app_secret)
shake_service = service.init_service('Shake')
```

Temporarily, I just finished the part of shaking without full tests.


##Log

2015-06-01

I removed the pylibmc because i want to let users choose what they want to cache
the access token, but by default, it always query from the api.
However, is there a better practise?

2015-05-29

The project can be used.

2015-05-27

I created the project.


## Finished tests
Tested interfaces:

+ \_get\_access_token
+ upload_picture
+ add\_new_page
+ edit_page
+ delete\_pages\_by_ids
+ apply_devices
+ edit\_device_info
+ bind\_the_page
+ find\_pages\_by_counts
+ find_devices


