python -V # 查看python版本

conda create -n <环境名> python=<版本> # 创建虚拟环境

conda remove -n <要删除的虚拟环境名> --all # all代表全删了；注意，如果你要删env1,不能在env1中删除env1,要么先conda deactivate env1 再删除，要么切换到别的虚拟环境后删除env1

conda list # 查看当前虚拟环境配置

conda env list # 查看有哪些虚拟环境

conda activate <虚拟环境名> # 切换到指定的虚拟环境

conda install ipykernel # 在当前环境中安装ipykernel

python -m ipykernel install  --name <>

jupyter kernelspec list # 查看jupyter notebook内部所有可供选择的内核及其路径

jupyter-kernelspec remove <insidename> # jupyter notebook中移除某个kernel注意别输入<>!!!;注意是某个kernel在jupyter notebook内部的名字，而不是在菜单上展示的名字！

python -m ipykernel install  --name <在jupyter notebook内部的名字> --display-name "在jupyter notebook 'change kernel'菜单展示的kernel名" # 注意，左边的双引号前有一个空格；不可以把python改为ipython

ipython kernel install --name "在jupyter notebook内部和菜单展示的kernel栏上相同的名字" --user

总结，要把某个指定的虚拟环境添加到jupyter notebook 的kernel :

(0.1):

打开anaconda3 prompt

(0.2):

conda env list # 查看已有的虚拟环境，记住你想要添加到jupyter notebook上的虚拟环境的名字

(1):

conda activate <指定的虚拟环境名> # 切换到指定的虚拟环境

(2):

conda install ipykernel # 在当前虚拟环境(指定的虚拟环境)下安装ipykernel

(3):

python -m ipykernel install  --name <name1> --display-name "name2" #注意别把<>打进去了！！;name1 是在jupyter notebook 内部用的内核名字，name2 是在jupyter notebook"change kernel"菜单栏上展示的名字

(4):

这时候打开jupyter notebook,在kernel 下拉菜单找到"change kernel"就能改变kernel 了

(5):

在anaconda3 prompt 输入：

jupyter kernelspec list 应该能看到name1已经被加入了











