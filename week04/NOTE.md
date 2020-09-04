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




# tips 1 pandas 中文资料

[pandas 中文链接](https://www.pypandas.cn/docs/getting_started/basics.html#属性与底层数据)
![](./pandas.png)

# tips 2 SQL基础教程

[SQL基础教程](https://www.w3school.com.cn/sql/sql_join_inner.asp)




作业背景：在数据处理的步骤中，可以使用 SQL 语句或者 pandas 加 Python 库、函数等方式进行数据的清洗和处理工作。

因此需要你能够掌握基本的 SQL 语句和 pandas 等价的语句，利用 Python 的函数高效地做聚合等操作。

作业要求：请将以下的 SQL 语句翻译成 pandas 语句：
复制代码

1. SELECT * FROM data;
	
2. SELECT * FROM data LIMIT 10;
	
3. SELECT id FROM data;  //id 是 data 表的特定一列
	
4. SELECT COUNT(id) FROM data;

5. SELECT * FROM data WHERE id<1000 AND age>30;

6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;

7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;

8. SELECT * FROM table1 UNION SELECT * FROM table2;

9. DELETE FROM table1 WHERE id=10;

10. ALTER TABLE table1 DROP COLUMN column_name;