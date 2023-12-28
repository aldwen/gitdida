
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
是一个origin 下游两个地址好，还是 用两个远端名，提交两次好？
"这是一行在gitee 上的编辑，会导致两个远端的仓库内容不一致，那么，会引发什么呢？"
我选用 两个远端仓库.

## 2023-12-23 22:21:03
tomato start.

## 2023-12-24 01:08:37
有一些心得的内容，还是不要记录在这里，或者记录在这里，也需要移走：

## logging 创建文件的问题
logging 模块可以自动创建文件，但是不能自动创建目录
```
log_file_name = f"logs/{datetime.now().strftime('%Y-%m')}.log"
```
在这里，如果 log 目录不存在，会导致报错，解决的办法是在 log.py 中确保目录创建成功。
```
log_file = Path(log_file_name)
log_file.parent.mkdir(parents=True, exist_ok=True)
```
对此，ChatGPT 给出的解答是：这种设计可能是为了避免在日志记录时在文件系统上创建过多的目录，因为这可能是意外的行为。在实际应用中，通常在初始化时就确保了日志文件所在的目录存在，这样可以避免这类问题。

嗯，在项目的内部，从一开始就要定义好logs 的目录。

## 2023-12-24 11:36:44
如果要生成命令行程序，需要另外用 pyinstall 进行打包。

tomato 开始

Done：程序找不到执行（测试）的流程，
Done：logger 记录在哪里？

## 2023-12-24 19:26:34
破案了。
我明明设置了默认的日志级别为 info，但是输出的却是 warning。终于发现，log.py 里，设置日志的次序是有影响的。我先设置了file_logger，这时他从默认logging 继承了级别: warning. 然后我再设置 logging.basicconfig . 是不能改写到 file_logger 设置的. 解决方法是 logging.basicConfig 要放在最前面。

## 2023-12-24 22:16:46
User
我遇到了一个问题，我使用 vscode 作为编辑器，连接到WSL 里的ubuntu 主机，然后当我编辑 log.py 文件后，调用 log.py 的文件并不会调用最新的修改，而是读取修改前的内容。如果我退出 vscode 再重新进去，将调用log.py 的最新版本。这是为什么？要如何修正
没有解决，将就着用....但是将来的DEBUG 还是可能被这个问题误导

## 2023-12-25 17:07:40 
logging 模块的问题最终得到了解决。我自己写的 config 找到了问题所在。官方的 config 示例也能完全看懂，并配置成功。
话费了很多时间。
开始编写 DoGit 的代码。

## 2023-12-26 00:08:40
还是没有开始编写 DoGit 的代码。
当我开始编写代码的时候，我会想到我应当先编写测试。在目前阶段，这是错误的想法。测试驱动开发（TDD）是非常有用的技能。但是，为了编写TEST，我们需要具备编写全流程代码的能力。Test 是代码的抽象，编写 Test 是比编写代码更高的能力。先编写出能跑完流程的代码，再去考虑 Test 的编写！

现在考虑DoGit代码的测试。
我们无法进入代码块内部进行测试，我们必须依赖于函数的返回值。因此，被测试的代码应当是函数，应当有返回值。这促进我代码的修改。
可以通过print将信息发送到控制台，pytest可以捕获print，但是这些print对程序运行不是必要的，这不是一个好办法。
我尝试通过log.info 将信息发送到控制台。但是，pytest 无法直接读取 logging 打印的信息。
通过caplog，我现在可以获取代码块的log信息，并进行对比。但是，我的测试代码变得很复杂：
```Python
def test_dojob_with_args(cli_runner: CliRunner, caplog):
    with caplog.at_level(logging.INFO):
        result = cli_runner.invoke(
            cmdline,
            ["--repository", "rrr", "--branch", "bbb", "--remote", "ooo"],
        )
        assert result.exit_code == 0
        assert any(
            "repository=rrr, work_branch=bbb, remote_name=ooo" in record.message
            for record in caplog.records
        )
        assert "Succeed" in caplog.text
        assert "dodida: executing additional steps..." in result.output
```
我感觉看懂测试代码都困难。
是否应当通过 mock 模块配置条件，从而只检查返回值？

## 2023-12-27 14:52:46
整理 doGit 的代码：
    调整log输出
    增加了没有更新不提交git的判断。
    配置文件里引入测试仓库地址。
问题：
    remote_name 获取失败 Done
    test 尚未编写。 Flase:找不到逻辑
    约定式提交需要自我整理一下。 Done

## 2023-12-27 18:48:15
Interval(dogit.py)：修改dogit 代码。

Done：
发现gitcommanderror 没有捕获到 repository 没有建立的错误。已经修改为giterror。
但是新的问题是，如何在信息里返回关于错误的更多的提示？

## 2023-12-27 22:39:19
tomato：开始考虑dodida.py。

## 2023-12-28 16:49:57
git 提交太多的问题还没有解决
大概读懂了task.py 的内容（但是对他维护两份变量列表表示不满）
摘录了一些对存储密码进行混淆的内容，有待实现。
需要进一步好好研究 如何生成我想要的 task ,以及，考虑作者的原思路，使用模版。




