from django.test import TestCase
import operaciones

class pruebas_unitarias(TestCase):

	def test_suma(self):
		self.assertEquals(operaciones.suma(5,5),10)
	def test_resta(self):
		self.assertEquals(operaciones.resta(5,5),0)
	def test_multiplicacion(self):
		self.assertEquals(operaciones.multiplicacion(5,5),25)
	def test_division(self):
		self.assertEquals(operaciones.division(5,5),1)