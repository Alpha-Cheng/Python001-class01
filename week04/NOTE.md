学习笔记

数据清洗很重要
在工作和生活中还没体会到应用的技巧和效果，接下来好好使用和练习

```python
#用于导出为.exl 的包 ~ xlwt
from sklearn import datasets #sklearn 数据集的包 ,引入数据集
# 鸢尾花数据集
iris = datasets.load_iris()
x,y = iris.data,iris.target

df.dropna() #处理数据集的缺失值
```
pandas have series and dataframe two datatype

datafrom  columns 列  index 行


