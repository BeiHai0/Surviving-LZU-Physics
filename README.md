希望可以帮到大家。

# 好文推荐

## 统计力学

[笔记 by WSLY](https://zhuanlan.zhihu.com/p/348728397)

[热力学知识点](https://zhuanlan.zhihu.com/p/69562371)

## 分析力学

[欧拉-拉格朗日方程推导](https://zhuanlan.zhihu.com/p/212584938)

[受周期性驱动力有阻尼一维谐振子](https://zhuanlan.zhihu.com/p/135856012)

[弹簧摆](https://zhuanlan.zhihu.com/p/664522639)

[带电粒子的E-L方程在电磁场规范变换下具有不变性](https://www.zhihu.com/question/552502390/answer/2666510475)

[单摆](https://zhuanlan.zhihu.com/p/68606317)

[“相空间”和“相流体”1](https://zhuanlan.zhihu.com/p/394303895)

[“相空间”和“相流体”2](https://zhuanlan.zhihu.com/p/394637504)

## 数理方法

[一致收敛和逐点收敛](https://wuli.wiki/online/UniCnv.html)

# markdown 配置

## "<>" 不成对出现

```
...\Programs\Microsoft VS Code\resources\app\extensions\markdown-basics
```

沿着上面路径，打开 language-configuration.json 文件，注释掉下面这一句：

```
{"open":"<","close":">","notIn":["string"]},
```

注释完应该像这样：

```
/* {"open":"<","close":">","notIn":["string"]}, */
```

关掉 VS code 再重新启动即可

## snippets

## 只保留自己的 snippetSuggestions，关闭 VS Code 自带的代码提示与补全功能

