
## 2023-12-20 
重新编写一遍这个项目，希望整理出完整的项目开发流程。

## 2023-12-20 17:21:18
先要建立项目框架

## 2023-12-20 19:33:38
TODO: github remote: Support for password authentication was removed on August 13, 2021.

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


