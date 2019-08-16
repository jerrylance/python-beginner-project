import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""测试name_function.py"""

	def test_first_last_name(self): #test开头的方法都会自动运行
		"""能够正确地处理像Janis Joplin这样的姓名吗？"""
		formatted_name = get_formatted_name('Janis', 'Joplin')
		self.assertEqual(formatted_name, 'Janis Joplin') #方法assertEqual，测试formatted_name是否等于'Janis Joplin'
# unittest.main() 可以测试不含有中间名的名字

	def test_first_last_middle_name(self):
		"""能够正确处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
		formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
unittest.main()

"""
常用的几种测试方法：
assertEqual(a,b)                # a,b相等
assertNotEqual(a,b)
assertTrue(x)
assertFalse(x)
assertIn(item, list)            # 核实item在list中
assertNotIn(item, list)         # 核实item不在list中

"""