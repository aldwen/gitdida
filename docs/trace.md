
## 2023-12-20 
重新编写一遍这个项目，希望整理出完整的项目开发流程。

## 2023-12-20 17:21:18
先要建立项目框架

## 2023-12-20 19:33:38
Done: github remote: Support for password authentication was removed on August 13, 2021.

remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.

## 2023-12-20 22:18:10
解决 github 连接失败。先用gitee。
引入 .editorconfig ，这都是现成的文件。
引入 dynaconf,done.
引入 logging，done。

Poetry 的版本管理功能很弱，可能还是要使用第三方包。
开始导入其他必要的包，不急，应当先编写测试。

## 2023-12-20 22:56:43
引入必要文件之：
cmdline.py
exceptiongs.py
tox.ini 这个文件肯定需要再改

继续恢复文件结构，尝试使用 pytest

尝试中，停在编写 test_verison.py这里。如何读取 pyproject.toml 的内容呢？

## 2023-12-21 00:11:00
咦，github 又能连接了，很神经。

Python项目版本控制研究。

https://zhuanlan.zhihu.com/p/521512177
本文介绍python项目的版本号迭代规则，以及github管理上 python项目的归档发布。通篇基于Semantic 和 python第三方库python-semantic-release。

## 2023-12-21 00:47:16
继续版本号的研究

## 2023-12-21 02:07:41
在编写第一个测试 test_version时，我就卡住了，importlib.metadata 无法获得项目的版本号，从23点到2点。chatGPT 和 Bard 都无法给出正确的解决答案。最后，在stack overflow提问时，我看到了类似问题，需要 进行 poetry install, 这样，poetry 就会安装 正在开发的项目，从而，importlib 就可以读取版本号了。唉.....
今晚到此为止。

## 2023-12-21 22:13:48

Done：test_version 应当断语不等于上一个版号
在VScode 中执行了测试。
在assert 后加"," 可以自定义错误信息

## 2023-12-21 23:05:18
研究 click 包，没有成功。

## 2023-12-22 19:42:50 - 2023-12-22 23:16:47
继续研究click 包
用了一个晚上时间看了click 的开头一小部分文档，但是够用。ChatGPT 帮助生成了 test_cmdline.py ，少写很多代码。
命令行入口可用了，今晚结束。

## 2023-12-23 21:29:25

TODO: 同时提交2个远端仓库，gitee 增加远端
