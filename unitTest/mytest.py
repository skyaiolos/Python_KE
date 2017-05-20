import unittest

def  add(a,b):
	return a+b

class MyTest(unittest.TestCase):
	def test_add(self):
		self.assertEqual(8,add(4,3))

if __name__ == '__main__':
	unittest.main()