

normal-mode:hjkl左下上右移动光标

:q! 强制退出，不保存修改

:wq 保存并退出vim

A(shift+a) 光标移动到行末并进入insert mode,可用于在行末追加写入.

normal mode: dw 光标放在所要删除的**单词**前，删除整个单词以及单词后的空格(后一个单词首字母会移动到光标后)

normal mode: de 光标放在所要删除的**单词**前，删除整个单词，但不删除单词后的空格.

normal mode: d$ 删除光标所在行内光标**以后**的所有字符，随后光标前跳一位

normal mode: w 光标跨过一个单词，移动到光标后第2个单词首字母前

normal mode: e 光标移动到光标后第一个单词的尾字母前

normal mode: 2w 执行两次w,光标跨过2个单词，移动到光标后第3个单词首字母前.

normal mode: 2e 执行两次e,光标移动到光标后第2个单词的尾字母前.

normal mode: 0 光标移动到行首.

 
