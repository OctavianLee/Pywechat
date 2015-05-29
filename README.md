# Wechat
Encapsulates wechat's APIs with Python.

Libs:

+ requests
+ pylibmc

``` python
pip install -r requirements.txt
```

Then you can use the Service.

Temporarily, I just finished the part of shaking without full tests.

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

Todo:

+ Impove codes
+ Add the service of card
+ Test interfaces