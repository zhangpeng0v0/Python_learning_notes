### 模块

~~~markdown
Python的模块是Python的程序文件

Python程序的构成：
		1. 顶层文件
				只有一个
		2. 模块（所有的子文件）
				模块可以调用其他模块
~~~

~~~markdown
1. 模块的概念：可以将代码量较大的程序分割成多个有组织，彼此独立但又能相互调用的代码片段，这些自我包含的有组织的代码块就是模块
2. 模块在物理形式上表现为以 .py 结尾的文件 
		1. 一个文件都可以被看做是一个模块
		2. 模块名的构成：
					包名.子包.文件名.py
		3. 包：是一种目录结构
				1. 包也是对象
				2. 包内可以有子包
				3. 包内必须有__init__.py文件（文件为空即可）
				4. 包内可以有模块
				5. 包是模块不可分割的一部分
						（包相当于模块的姓氏）
		4. 使用模块时，必须使用全名（包名.子包名.模块名）
3. Python允许通过导入的形式引入其他模块到当前文件中使用
		将独立的文件之间组织成更大的程序
4. 模块的全局成员都会在被导入时变成模块的属性
~~~

* 模块的导入

~~~markdown
1. 包： package
		1. 包也是对象
        2. 包内可以有子包
        3. 包内必须有__init__.py文件（文件为空即可）
        4. 包内可以有模块
        5. 包是模块不可分割的一部分
        （包相当于模块的姓氏）
2. 关键字：import


导入形式：
1. import 包路径.模块名   ---没有后缀
		1. 发声命名冲突的概率低，即便模块中的属性名和当前文件中的变量发生了命名冲突，不会影响使用（因为有包名的限制）
		2. 在整个文件中的使用，必须都写全名
		3. 该形式不能导入包以下级别的内容
		4. 如果引入多个模块，用逗号隔开
2. from 包路径.模块名 import 属性名
		1. 声明import后的属性名都是来自于包路径+模块名的
		2. 如果该文件中有同名变量，则会发生命名冲突
		3. 如果引入多个模块，则只能使用多个from...import
		4. 如果同一个模块引入多个属性，则可以在import后用逗号隔开
		5. 可以导入模块级别的内容
3. import 包路径.模块名 as 别名
		1. 引入多个模块时，要分开起别名
		2. 别名不能和该文件中的其他变量发生命名冲突
4. from 包路径.模块名 import 属性名 as 别名
		1. 别名不能和该文件中的其他变量发生命名冲突
		2. 引入多个属性时，要分开起别名

3. 通配符：* 
		通配模块下的多个属性 
		不建议使用---可读性差
~~~

* 模块的作用

~~~markdown
1. 各司其职
2. 可重用性
3. 可读性高
4. 减少代码冗余
~~~

---

* __name\_\_

~~~markdown
1. if __name__=='__main__':
		#代码
如果当前文件的name属性为__mian__则执行代码块中的代码，否则不执行
		利用以上形式做模块的测试代码

2. 任何模块在被导入时，会自动执行一次
		原理：
		1. 相当于在当前文件中创建了一个模块对象
		2. import：加载模块对象
3. 模块中，尽量不要书写任何逻辑代码和函数的调用或对象的创建：
		逻辑代码：通过某种逻辑执行的代码
		（if-else,for,while）
		逻辑代码，应该书写在代码块中
		
		尽量写：1. 全局变量  2. 函数  3. 类
4. 当主流程在模块中时，模块中的__name__属性为：__main__,当主流程在其他模块中时，被引入的模块的__name__属性为模块的全名

~~~

---

* 搜索路径

~~~Markdown
模块：sys
path属性：记录了python中所有的路径
		引入的模块，在path中则可以使用，不再path中则不能使用
1. sys.path 中有一个路径：site-packages
		只存储第三方模块
		模块的分类：
		1. 自带模块（标准库）
		2. 自定义模块
		3. 第三方模块（django，flask,numpy,pandas,scrapy,xpath,scipy）
~~~

---

### Python的执行架构

~~~markdown
Python程序的构成：
		模块+顶层文件
python中的标准库：自带模块---电池  
		cheese shop：145000个类库
Python的社区：
		派派社区：
		https://pypi.python.org/pypi
查看标准库：
		help(‘modules’)
~~~

* Python的执行环境

~~~markdown
1. 尽量只让模块保留：全局变量，类，函数
2. 查看文档---Library Reference
3. PEP规范：
		Python Enhancement Protocols ：Python增强建议书
		PEP1：规定了PEP本身的规范
	    *PEP8：定义了Python代码的风格
	    PEP333：Web开发的风格
	    PEP3000：规定了Python3相关技术规格
	    
	    网址：https://www.python.org/dev/peps/
~~~

---

