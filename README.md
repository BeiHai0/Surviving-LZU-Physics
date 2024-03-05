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

## 量纲

[自然单位制?](https://physics.stackexchange.com/questions/102527/how-can-planck-units-be-consistent-with-conflicting-dimensions-of-mass)

# markdown 配置

## "<>" 不成对出现

```
...\Microsoft VS Code\resources\app\extensions\markdown-basics
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

```
...\Microsoft VS Code\resources\app\extensions\markdown-basics
```

按以上路径走，打开 language-configuration 文件，加上下面这句（要加在最外面的大括号内部，并且注意上一句末尾加个逗号）：

```
    "[markdown]":{
         "editor.quickSuggestions":true
    }
```

加完之后应该长这样：

```
{
    "comments":{"blockComment":["<!--","-->"]},

    "brackets":[["{","}"],["[","]"],["(",")"]],

    "colorizedBracketPairs":[],

    "autoClosingPairs":[{"open":"{","close":"}"},

    {"open":"[","close":"]"},{"open":"(","close":")"},

    /* {"open":"<","close":">","notIn":["string"]},

    */{"open":"`","close":"`"},

    {"open":"```","close":"```"}],

    "surroundingPairs":[["(",")"],["[","]"],["`","`"],["_","_"],["*","*"],["{","}"],["'","'"],["\"","\""]],

    "folding":{"offSide":true,"markers":{"start":"^\\s*<!--\\s*#?region\\b.*-->",
    
    "end":"^\\s*<!--\\s*#?endregion\\b.*-->"}},
    
    "wordPattern":{"pattern":"(\\p{Alphabetic}|\\p{Number}|\\p{Nonspacing_Mark})(((\\p{Alphabetic}|\\p{Number}|\\p{Nonspacing_Mark})|[_])?(\\p{Alphabetic}|\\p{Number}|\\p{Nonspacing_Mark}))*","flags":"ug"},

    "[markdown]":{
         "editor.quickSuggestions":true
    }
}
```

重启 VS Code 即可使用自定义的 snippets

## 个人惯用 markdown snippets

注意：

所有连续出现两个 “\” 的地方，第一个 “\” 起转义作用

在行内或行间公式使用的 snippets 不能把 scope 设置为 markdown。scope 那行直接删掉或注释掉即可。

