学习笔记

作业要求：

使用 Django 的 Form、Auth 组件，实现用户登录和密码验证功能。

要求：

1. 登录界面要求能够输入用户名、密码，且密码需大于 8 位。
2. 用户名、密码通过 Django 的 Auth 组件对数据库中预先存储的用户密码进行验证。
3. 如果登录失败提示用户密码错误，登录成功后跳转到首页（或其他非登录的页面）。


# 作业实现步骤

1. 使用命令创建Django项目

   ```shell
   django-admin startproject MyDjango
   ```

2. 使用命令创建Django应用

   ```Shell
   python manage.py startapp myapp
   ```

3. 修改配置settings.py
  - 将自己的应用追加到末尾
  - 修改数据库配置
    ```python
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        }
    }
    ```

4. 在项目的路由文件urls.py中添加自己应用要使用的路由文件路径
    ```python
    path('',include('myapp.urls'))
    ```

5. 准备要使用的用户名密码
  - 在数据库中创建要使用到的表,通过下面命令自动创建Django默认使用的用户表
  ```shell
  python manage.py makemigrations 
  python manage.py migrate
  ```
  - 创建Django管理员用户
  ```Shell
  python manage.py createsuperuser
  ```
  - 进入Django交互环境，创建等下使用来登录的用户
  ```shell
  python manage.py shell
  from django.contrib.auth.models import User
  user = User.objects.create_user('test', 'test@test.com', 'testpasswd')
  ```

6. 创建登录页面的表单
```python
from django import forms
class LoginForm(forms.Form):
    user_name = forms.CharField(label="用户名")
    passwd = forms.CharField(widget=forms.PasswordInput, min_length=8, label="密码")
```

7. 编写视图函数
```python
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from .form import LoginForm
def login_demo(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['user_name'], password=cd['passwd'])
            if user:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'fail.html', {'form': login_form})
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'login.html', {'form': login_form})
```

8. 在自己应用的文件夹下添加步骤4中指定的路由文件
```Python
from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_demo)
]
```

9. 模板添加和样式添加

```html
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8" />
        <title>主页</title>
        {% load static %}
        <link rel="stylesheet" href="{% static 'myapp/static/demo.css' %}" >
    </head>
    <body>
        <script>

            var box = document.getElementsByClassName('textCon')[0];
            function init() {
                var width = box.offsetWidth;
                var count = parseInt(width / 50 * 5);
                for (var i = 0; i < count; i++) {
                    var size = parseInt(ran(60, 120) / 10);
                    var ele = document.createElement('div');
                    ele.classList.add('item');
                    ele.style.width = size + 'px';
                    ele.style.height = size + 'px';
                    ele.style.left = ran(0, 95) + '%';
                    ele.style.top = ran(20, 80) + '%';
                    ele.style.animationDelay = ran(0, 30) / 10 + 's';
                    box.appendChild(ele);
                }
            }
            function ran(min, max) {
                min = parseInt(min);
                max = parseInt(max);
                return Math.floor(Math.random() * (max - min + 1)) + min;
            }
            init();
        
        </script>
        <p>如果什么也没有显示的话，就代表前端样式没设置好...</p>
    </body>
    </html>
```
python manage.py runserver