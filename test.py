import unittest
import  prime_num


class Prime_numTestCase(unittest.TestCase):
	def setUp(self):
		self.prime = Prime_num()
	
	def tearDown(self):
		del self.prime		
	
	def test_validity(self):
		self.assertEqual(prime.Prime_num(2))
	
	def test_num_less_than_zero(self):
		self.assertEqual(prime.Prime_num(-1))
	
	def test_value_is integer(self):
		self.assertEqual(prime.Prime_num("") msg"Only integers allowed")
	
	def test_it_returns_correct_outputs(self):
		self.assertEqual(prime.Prime_num(5), True)


		


