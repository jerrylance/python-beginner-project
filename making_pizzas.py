# 使用import语句指定模块名
# import 让python打开pizza2.py文件，并将其中的所有函数都复制到这个程序中
import pizza2

# 我们想要调用pizza2.py文件里的make_pizza函数
# 指定 模块名字 + 函数名，记得用句号.隔开
# module_name.fuction_name()

pizza2.make_pizza(16, 'pepperoni')
pizza2.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



# 第二种

# from module_name import function_name

# from module_name import function_0, function_1, function_2

from pizza2 import make_pizza

# 不用句号

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



# from module_name import fuction_name as fn
# 给函数make_pizza指定了别名mp()
from pizza2 import make_pizza as mp

# 调用函数make_pizza()时，可简写为mp()
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')



# import module_name as mn
# 更加简洁，适合长名字的模块或函数
# 给模块pizza指定别名p
import pizza2 as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# from module_name import *
# 使用星号* 让python导入模块中的所有函数
# 因为是导入了每个函数，所以我们可以通过名称来调用每个函数
from pizza2 import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
