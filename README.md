# SEU-Badminton-Hall-Appointment
Badminton Hall Appointment tool

东南大学羽毛球馆预约工具

羽毛球馆老是约不上，所以我写了一个小工具，方便挂机预约场馆

整个软件分成三个部分，登录，验证，预约

首先是登录，场馆预约网站本身安全性比较高，我短时间想不到什么方法可以登录，但是东南大学本身有一些原来的网站入口，新版本的入口不好进入，但是原来的
非常容易，所以我使用了其中一个入口。

验证部分，场馆预约网页在预约时加入了验证码，但是比较简单，是基本的数字验证码，我从网上找到了基本数字图片，加上python本身的图片识别库，很简单的
破解了验证码，具体过程可以看源代码。

预约部分，这部分主要是报文的构成，主要是日期，时间，类型，几个简单的参数。

new badminton是基于qt开发的，原来的是其他人写的，现在已经不能使用，可以参考。

![image](https://github.com/apxlin/SEU-Badminton-Hall-Appointment/blob/master/badminton.png)

