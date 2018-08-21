## 如何把我们写的python程序定义成一个模块并进行后续的使用？
### - QuSusu
### - 2018/08/21
### - qususu2012@126.com


### - 学习主要参考链接：
- [手把手教你自己写一个Python模块，并将其发布并安装到自己的Python环境中去](https://blog.csdn.net/coolcooljob/article/details/80082907)
- [亲自动手写一个python库（二)](https://www.jianshu.com/p/81d20ccf5d13)，以后进阶设置也可以参考这个


---
### First, 明确一些概念：

- package，包
	- module，模块，就是很多个py文件组成了模块；
		- .py文件

---

### Secondly, 对写好的py文件打包：

- 先写一个.py的文件：
	- `generate_corr_plot.py`
- 建立一个文件夹：
	- `my_package`
- 将自己写的.py文件放到这个文件夹下面;
- 在这个文件夹下创建一个`__init__.py`文件;
- 在`my_package`的同级目录下创建一个`setup.py`文件，文件内容如下：
		
		from setuptools import setup, find_packages
		
		setup(
		name='generate_corr_plot.py',
		version='1.0', author='QuSusu',
		packages = find_packages(),
		include_package_data = True,
		platforms = 'any',
		install_requires = [],
		)

- 好了，现在看一下目录结构：

		├── my_package
		│   ├── generate_corr_plot.py
		│   └── __init__.py
		└── setup.py
- 程序打包，生成用于发布的压缩包：
	- `python setup.py sdist`
	- 此时在根目录出现了dist文件夹，里面有`generate_corr_plot.py-1.0.tar.gz`这个文件，这就是我们生成的压缩包了（可用于发布到PyPI上）。

---

### Thirdly,对2中打包好的文件在自己的python环境下import使用：
- 解压打包好的压缩包：
	- `tar -zxvf generate_corr_plot.py-1.0.tar.gz`

- install 安装到自己的python目录下：
	- `python setup.py install`

- import使用测试吧！

---
