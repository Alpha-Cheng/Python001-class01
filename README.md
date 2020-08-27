# 极客大学「Python进阶训练营-第1期」作业提交仓库

## 讲师课件下载地址

请大家通过该链接查看讲师课件并进行下载， 链接: https://pan.baidu.com/s/1bwl0b6ooKKzBi0tc_MCB_w 密码:1iu4


## 仓库目录结构说明

1. `week01/` 代表第一周作业提交目录，以此类推。
2. 请在对应周的目录下新建或修改自己的代码作业。
2. 每周均有一个 `NOTE.md` 文档，你可以将自己当周的学习心得以及做题过程中的思考记录在该文档中。

## 作业提交规则
 
1. 先将本仓库 Fork 到自己 GitHub 账号下。
2. 将 Fork 后的仓库 Clone 到本地，然后在本地仓库中对应周的目录下新建或修改自己的代码作业，当周的学习总结写在对应周的NOTE.md文件里。
3. 在本地仓库完成作业后，push 到自己的 GitHub 远程仓库。
4. 最后将远程仓库中当周的作业链接，按格式贴到班级仓库对应学习周的issue下面。
5. 提交issue请务必按照规定格式进行提交，否则作业统计工具将抓取不到你的作业提交记录。 


### Review 与点评
1. 助教会Review并点评大家的作业。
2. 你也可以看到其他同学的作业，取长补短。

## 注意事项
 如果对 Git 和 GitHub 不太了解，请参考 [Git 官方文档](https://git-scm.com/book/zh/v2) 或者极客时间的[《玩转 Git 三剑客》](https://time.geekbang.org/course/intro/145)视频课程。

```python
    pyautogui & pywinauto 用于协作 windows 的包
    xlrd 读取 excel2013以上版本的 .exl
    read_excel 最高支持 excel2013 的 .exl
    pip install pypiwin32 读取 .exl
    pandas 打开 .exl pd.read_excel(password) ~ 如果加密的话，需要写密码参数

    win32com.client.Dispatch('Excel.Application') 的确可以去除密码
```