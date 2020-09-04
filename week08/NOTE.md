学习笔记

1. 变量的赋值：
    * 连等的赋值是内存地址的拷贝和重定向`a=[1,2,3],b=c=a,print(id(a),id(b),id(c))`
    * 重新开辟一个数据值赋值给原变量，是修改变量原来的地址指向为现在的地址指向，`a=[1,2,3],b=a,a[4,5,6]`
    * 修改数组元素的方法 `a=[1,2,3], b=a, a[0]=4,a[1]5,a[2]=6`
    * 可变数据类型 list，dict; --改变数据内容会地址扩充或缩减，不改变原对象的起始地址
    * 不可变数据类型 int,float,string,tuple; --改变数据内容的时候会新建地址的对象
2. 序列分类 
    * 容器序列：list、tuple、collections.deque 等，能存放不同类型的数据容器序列可以存 放不同类型的数据。 
    * 扁平序列：str、bytes、bytearray、memoryview (内存视图)、array.array 等，存放的 是相同类型的数据扁平序列只能容纳一种类型
    * 容器序列存在深拷贝、浅拷贝问题 • 注意：非容器（数字、字符串、元组）类型没有拷贝问题
    ```
        old_list = [ i for i in range(1, 11)]

        new_list1 = old_list
        new_list2 = list(old_list)

        # 切片操作
        new_list3 = old_list[:]

        # 嵌套对象
        old_list.append([11, 12])


        import copy
        new_list4 = copy.copy(old_list)
        new_list5 = copy.deepcopy(old_list)

        assert new_list4 == new_list5 #True
        assert new_list4 is new_list5 #False AssertionError

        old_list[10][0] = 13

    #import copy 
    #copy.copy(object) #地址复制
    #copy.deepcopy(object) #重新开辟一个对象和内存地址

    ```

    * 另一种分类方式 ：
        * 可变序列list、bytearray、array.array、collections.deque 和memoryview。
        * 不可变序列tuple、str 和bytes
3. 函数需要关注什么 
    * 调用 对象，对象的执行（）
    * 作用域 - 命名空间 
        * 高级语言对变量的使用：  
            * 变量声明 
            * 定义类型（分配内存空间大小） 
            * 初始化（赋值、填充内存） 
            * 引用（通过对象名称调用对象内存数据）
        * Python和高级语言有很大差别，在模块、类、函数中定义，才有作用域的概念。
        * Python 作用域遵循LEGB规则。
            * LEGB 含义解释： 
                * L-Local(function)；函数内的名字空间 
                * E-Enclosing function locals；外部嵌套函数的名字空间（例如closure） 
                * G-Global(module)；函数定义所在模块（文件）的名字空间  
                * B-Builtin(Python)；Python 内置模块的名字空间
    * 参数 
        * 高阶：参数是函数、返回值是函数 常见的高阶函数：map、reduce、   filter、apply apply 在Python2.3被移除，reduce 被放在functools包中 推导式和生成器表达式可以替代map 和filter 函数 
        ```
            import functools
            add_1 = functools.partial(add, 1)
            add_1(10)

            import itertools
            g = itertools.count()
            next(g)
            next(g)
            auto_add_1 = functools.partial(next, g)
            auto_add_1()
        ```
    * 返回值 



    作业一：

区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：

    list
    tuple
    str
    dict
    collections.deque

作业二：
自定义一个 python 函数，实现 map() 函数的功能。

作业三：
实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。