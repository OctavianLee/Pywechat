# Pywechat
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Octavianlee/Pywechat/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/Octavianlee/Pywechat/?branch=master)
[![Build Status](https://scrutinizer-ci.com/g/OctavianLee/Pywechat/badges/build.png?b=master)](https://scrutinizer-ci.com/g/OctavianLee/Pywechat/build-status/master)


A python SDK for the wechat public platform.
微信公众平台api sdk


ALL APIs are from https://mp.weixin.qq.com/wiki/home/index.html

If you have any advices, just open an issue or email me!

If you wants to fix the code or help me complete the whole project, just send me
the pull request!


## Todo List

+ Impove the code
+ Test the code
+ Fix bugs
+ Write comment for methods
+ Add a new service(Later...)


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

Without Tests Now, it might have some bugs in the code.

##Update Logs

2015-06-04
BUG FIX

2015-06-03

I refactored the project and added the exceptions in the code. It is a big change.


2015-06-02

I have finished the part of card management without test.Now I will focus on
improving codes and adding the tests.That will be a great job!


2015-06-01

I removed the pylibmc because i want to let users choose what they want to cache
the access token, but by default, it always query from the api.
However, is there a better practise?

2015-05-29

The project can be used.

2015-05-27

I created the project.

