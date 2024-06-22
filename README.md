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

## snippets

## 个人惯用 markdown snippets

注意：

所有连续出现两个 “\” 的地方，第一个 “\” 起转义作用

在行内或行间公式使用的 snippets 不能把 scope 设置为 markdown。scope 那行直接删掉或注释掉即可。

```
{
	// Place your global snippets here. Each snippet is defined under a snippet name and has a scope, prefix, body and 
	// description. Add comma separated ids of the languages where the snippet is applicable in the scope field. If scope 
	// is left empty or omitted, the snippet gets applied to all languages. The prefix is what is 
	// used to trigger the snippet and the body will be expanded and inserted. Possible variables are: 
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. 
	// Placeholders with the same ids are connected.
	// Example:
	// "Print to console": {
	// 	"scope": "javascript,typescript",
	// 	"prefix": "log",
	// 	"body": [
	// 		"console.log('$1');",
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }

	"行间公式": {
		"scope":"markdown",
		"prefix":".m",
		"body":[
			"$$",
			"$0",
			"$$"
		],
		"description":"行间公式"
	},

	"行内公式": {
		"scope":"markdown",
		"prefix":".i",
		"body":[
			"$$0 $"
		],
		"description":"行内公式"
	},

	"Aligned":{
		"scope":"markdown",
		"prefix":".ali",
		"body":[
			"$$",
			"\\begin{aligned}",
			"$0",
			"\\end{aligned}",
			"$$"
		],
		"description":"Aligned"
	},

	"Mathrm":{
		//"scope":"markdown",
		"prefix":".rm",
		"body":[
			"\\mathrm{$0}",
		],
		"description":"Mathrm"
	},

	"Big Left Bracket":{
		"scope":"markdown",
		"prefix":".{",
		"body":[
			"$$",
			"\\left\\{",
			"\\begin{aligned}",
			"$0",
			"\\end{aligned}",
			"\\right.",
			"$$"
		],
		"description":"Big Left Bracket"
	},

	"Begin Cases": {
		"scope":"markdown",
		"prefix":".bc",
		"body":[
			"$$",
			"\\begin{cases}",
			"$0",
			"\\end{cases}",
			"$$"
		],
		"description":"Begin Cases"
	},

	"Mathscr": {
		//"scope":"markdown",
		"prefix":".scr",
		"body":[
			"\\mathscr{$0}"
		],
		"description":"Mathscr"
	},

	"Mathcal": {
		//"scope":"markdown",
		"prefix":".cal",
		"body":[
			"\\mathcal{$0}"
		],
		"description":"Mathcal"
	},

	"Longrightarrow": {
		//"scope":"markdown",
		"prefix":".lra",
		"body":[
			"\\Longrightarrow"
		],
		"description":"Longrightarrow"
	},

	"varepsilon": {
		//"scope":"markdown",
		"prefix":".veps",
		"body":[
			"\\varepsilon"
		],
		"description":"varepsilon"
	},

	"Bigg[]": {
		// "scope":"markdown",
		"prefix":".b[",
		"body":[
			"\\bigg[ $1 \\bigg] $0"
		],
		"description":"Bigg[]"
	},

	"Bigg()": {
		// "scope":"markdown",
		"prefix":".b(",
		"body":[
			"\\bigg( $1 \\bigg) $0"
		],
		"description":"Bigg[]"
	},

	"Bigg Vertical Line": {
		//"scope":"markdown",
		"prefix":".vl",
		"body":[
			"\\bigg|_{$0}"
		],
		"description":"Bigg Vertical Line"
	},

	"bmatrix": {
		//"scope":"markdown",
		"prefix":".bm",
		"body":[
			"\\begin{bmatrix}",
			"$0",
			"\\end{bmatrix}"
		],
		"description":"bmatrix"
	},

	"vmatrix": {
		//"scope":"markdown",
		"prefix":".vm",
		"body":[
			"\\begin{vmatrix}",
			"$0",
			"\\end{vmatrix}"
		],
		"description":"vmatrix"
	},

	"pmatrix": {
		//"scope":"markdown",
		"prefix":".pm",
		"body":[
			"\\begin{pmatrix}",
			"$0",
			"\\end{pmatrix}"
		],
		"description":"pmatrix"
	},

	"mathbb": {
		//"scope":"markdown",
		"prefix":".bb",
		"body":[
			"\\mathbb{$0}"
		],
		"description":"mathbb"
	},

	".lb": {
		//"scope":"markdown",
		"prefix":".lb",
		"body":[
			"\\left\\{",
			"\\begin{aligned}",
			"$0",
			"\\end{aligned}",
			"\\right."
		],
		"description":"bra"
	},

	"DC": {
		//"scope":"markdown",
		"prefix":".dc",
		"body":[
			"\\mathop{\\leftrightarrow}\\limits^{\\mathrm{DC}}"
		],
		"description":""
	},

	"bold": {
		//"scope":"markdown",
		"prefix":".bd",
		"body":[
			"\\bold{$1}$2"
		],
		"description":"bold"
	},

	"sinc": {
		//"scope":"markdown",
		"prefix":".sinc",
		"body":[
			"\\mathrm{sinc}($0)"
		],
		"description":"sinc"
	},

	"ps": {
		//"scope":"markdown",
		"prefix":".ps",
		"body":[
			"\\{$0 \\\\}"
		],
		"description":"ps"
	},

	"displaystyle": {
		//"scope":"markdown",
		"prefix":".ds",
		"body":[
			"$\\displaystyle{$1 }$ $2"
		],
		"description":""
	},

	"矩阵表示": {
		//"scope":"markdown",
		"prefix":".mr",
		"body":[
			"\\mathop{=}\\limits^{$1 }$2"
		],
		"description":"某一表象下的矩阵表示"
	},

	"big ps": {
		//"scope":"markdown",
		"prefix":".bps",
		"body":[
			"\\bigg\\{$1 \\bigg\\\\} $2"
		],
		"description":"big ps"
	},

	"": {
		"scope":"markdown",
		"prefix":"",
		"body":[
			
		],
		"description":""
	},
	

}
```

