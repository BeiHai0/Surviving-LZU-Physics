## 矩阵：

[] #标识为矩阵

逗号或空格分隔元素

; 换行

\* //矩阵乘法

format long #切换到长浮点数表示

format short #切换到短浮点数表示

zeros(m,n) #创建m行n列零矩阵

ones(m,n) //创建m行n列元素为1的矩阵

rand(m,n) //创建m行n列矩阵，元素取值在(0,1)之间

可用单值函数或单一运算符，同时处理矩阵中的所有元素

matrix' //转置矩阵

inv(matrix) //matrix 的逆矩阵

matrix1.*matrix2 //元素级乘法

matrix.^3 //元素级幂运算

matrix1./matrix2 //元素级除法

[matrix1,matrix2] //横向串联两个矩阵

[matrix1;matrix2] //纵向串联两个矩阵

## 复数

表示复数的虚部用i或j

## 数组/矩阵索引

**Matlab索引从1开始**

matrix(i,j) //行列下标索引

matrix(n) //单一下标索引，按列：先第一列，后第二列，……

不可在赋值语句右侧数组外部元素

可在赋值语句左边引用数组外部元素并对其赋值，数组会被扩充

matrix(start:end,column) //取matrix 的column列 start 元素直到end元素

matrix(row,start:end) //取matrix 的row行 start元素指导end元素

单独的冒号代表取该维中的所有元素

matrix(:,column) //取matrix 的column列

matrix(row,:) //取matrix 的row行

matrix = start:step:end //创建等间距向量并赋值给matrix

matrix = start:end //默认步长step=1

## 工作区变量

whos //查看工作区变量

whos a //查看变量a

退出matlab后，工作区变量**不保存**

clear //清除工作区变量

save filename.mat //将工作区保存在当前工作文件夹中一个名为 MAT 文件的压缩文件中

load filename.mat //将 MAT 文件中的数据还原到工作区

## 文本和字符

t = "hello,world!" //双引号包裹string类;将字符序列括在双引号中,可以将文本赋给变量

t = "hello"",""world!"  如果文本包含双引号，要在定义中使用两个双引号

t = "hello,world!"+1+"0" //输出："hello,world10"//要将文本添加到字符串的末尾，要使用加号运算符 +

strlength(a) //求字符串a的长度

strlength(matrix) //对字符串矩阵matrix的每个元素求长度，以矩阵形式输出

seq = 'ATGCCGGA' //char类，字符数组

seq(4) //返回'C' //

string 和char 对比：

s1 = "123"

s2 = '456'

s1(1)

s2(2)


拟合曲线：

x是自变量数组，y是因变量数组，n是拟合所用多项式函数的最高次数，

```
p = polyfit(x,y,n)
```

polyfit(x,y,n)返回一个数组，返回的数组先后储存最高次项前的系数$\cdots$常数项

```
x=[]
y=[]
p=polyfit(x,y,n)
x1=[]
y1=polyval(p,x1)
plot(x1,y1)
```

title("")

xlabel("")

ylabel("")

array./2 # 元素级除法

```
.* # 元素乘法
* # 矩阵乘法
./ 
.^ # 按元素求幂
^ # 矩阵求幂

```

多项式积分：

```
q = polyint(p) # polyint(p)返回不定积分的多项式系数数组；p为被积多项式的系数数组
I = diff(polyval(q, [a,b])) # 计算差值
```

条件语句：

```
if 

end
```

循环语句：

```
for i = a:step:b

end
```

填充数组：

```
p = padarray(A, size, 填充物, 填充方式 ) # 用填充物对 A 进行填充
```

在坐标图上标定点的坐标：

```
text([x1,x2],[y1,y2],{s1,s2})
```



