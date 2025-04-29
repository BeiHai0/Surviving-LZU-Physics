希望可以帮到大家。

# Licence

Surviving-LZU-Physics by BeiHai0 is marked with CC0 1.0 Universal 

https://creativecommons.org/publicdomain/zero/1.0/deed.en

# 必备软件

- [Chrome](https://www.google.cn/intl/zh-CN/chrome/)

- 科学上网工具（可以请教身边的同学）

- [VScode](https://code.visualstudio.com/)

- [git](https://git-scm.com/)：安装的时候若无特殊需求，一直“下一步”即可。

- [百度网盘](https://pan.baidu.com/download#win)：虽然特别恶心，但没办法。

- [Mathematica](https://tiebamma.github.io/InstallTutorial/)：有能力的话请支持正版。

- [Anaconda](https://www.anaconda.com/download/success)

- [Office](http://msweb.lzu.edu.cn/download/office2021.html)

## git 配置

> 假设你已经有了远程库，但想在新电脑的某个文件夹中（以桌面为例）继续写东西并推送到远程库。

- 桌面空白处鼠标右键

- Open Git Bash here

- 此时会打开 git bash，输入：

```
git config --global user.name "Your Name"
```

- 回车。再输入：

```
git config --global user.email "Your Email"
```

- 回车。

注意把 "Your Name" 和 "your Email" 替换成你的名字和邮箱。

> 下面就不提醒回车了。

- 输入：

```
ssh-keygen -t rsa -b 4096 -C "Your Email"
```

注意把 "your Email" 替换成你的邮箱。

如无特殊需求，接下来：

- 回车。

- 回车。

- 回车。

这样就生成了 SSH 密钥。

- 此电脑 $\to $ OS(C:) $\to  $ 用户 $\to $ 你的用户名 $\to $ .ssh 文件夹 $\to $ id_rsa PUB 文件 $\to $ 右击，打开方式选择“记事本打开” $\to $ 键盘上 Ctrl + A，Ctrl + C 复制

- 到 github 官网找到你的远程仓库。

- Setting $\to $ Deploy Keys $\to $ Add deploy key

- "Title" 自己取，在 "Key" 中键盘上按 Ctrl + V 把你刚刚复制的东西粘贴进去。

- 勾选 "Allow write access"

- 点击 "Add key"

这样就可以往远程仓库推送东西了。

- 点击 <>Code

- 点击绿色的 <>Code

- 把你的远程仓库的 SSH 地址复制到剪贴板中

- 回到 git bash，输入：

```
git clone YourURL
```

注意 YourURL 处可以右键 Paste 进行粘贴。 

这样就把远程库克隆到本地了。

现在可以在本地写东西，写完后：

```
git add .

git commit -m"描述"

git push origin master
```

就可以把本地的提交推送到远程仓库了。

# markdown 配置

## settings.json文件

- 打开 VScode

- 点击左下角齿轮图标

- Settings

- 点击右上角纸张翻页图标（open settings）打开 settings.json 文件。

下面是个人习惯的配置，可以参考。

```
{
    "workbench.colorTheme": "Visual Studio Light",
    "[markdown]": {
        "editor.unicodeHighlight.nonBasicASCII": false,
        "editor.formatOnSave": true,
        "editor.renderWhitespace": "all",
        "editor.wordWrap": "on",
        "editor.quickSuggestions": {
        "strings": false,
        "comments": false,
        "other": false
        }
    },
}
```

## snippets

- 打开VScode

- 点击左下角齿轮图标

- Snippets

- New Global Snippets Profile

## 个人惯用 markdown snippets

注意：

所有连续出现两个 “\” 的地方，第一个 “\” 起转义作用

在行内或行间公式使用的 snippets 不能把 scope 设置为 markdown。scope 那行直接删掉或注释掉即可。

下面是个人惯用 snippets，可以参考。

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

	"$$ $$": {
		//"scope":"markdown",
		"prefix":".m",
		"body":[
			"$$",
			"$0",
			"$$"
		],
		"description":"$$ $$"
	},

	"$ $": {
		"scope":"markdown",
		"prefix":".i",
		"body":[
			"$$0 $"
		],
		"description":"$ $"
	},

	"Aligned":{
		//"scope":"markdown",
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
			"\\mathrm{$1}$2",
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
		"prefix":".Lra",
		"body":[
			"\\Longrightarrow"
		],
		"description":"Longrightarrow"
	},

	"longrightarrow": {
		//"scope":"markdown",
		"prefix":".lra",
		"body":[
			"\\longrightarrow"
		],
		"description":"longrightarrow"
	},

	"varepsilon": {
		//"scope":"markdown",
		"prefix":".veps",
		"body":[
			"\\varepsilon"
		],
		"description":"varepsilon"
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
			"\\left\\{$1 \\right\\\\}$2"
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
			"\\xlongequal{$1 } $2"
		],
		"description":"矩阵表示"
	},

	"empty set": {
		//"scope":"markdown",
		"prefix":".vn",
		"body":[
			"\\varnothing"
		],
		"description":"empty set"
	},
	
	"()": {
		//"scope":"markdown",
		"prefix":".p",
		"body":[
			"\\left($1 \\right)$2"
		],
		"description":"()"
	},

	"frac": {
		//"scope":"markdown",
		"prefix":".f",
		"body":[
			"\\frac{$1 }{$2 } $3"
		],
		"description":"frac"
	},

	"longleftrightarrow": {
		//"scope":"markdown",
		"prefix":".llra",
		"body":[
			"\\longleftrightarrow"
		],
		"description":"longleftrightarrow"
	},

	"abs": {
		//"scope":"markdown",
		"prefix":".abs",
		"body":[
			"\\left|$1 \\right|$2"
		],
		"description":"abs"
	},

	"[]": {
		//"scope":"markdown",
		"prefix":".[",
		"body":[
			"\\left[$1 \\right]$2"
		],
		"description":"[]"
	},

	"Lie": {
		//"scope":"markdown",
		"prefix":".lie",
		"body":[
			"\\mathfrak{$1 }$2"
		],
		"description":"Lie "
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



