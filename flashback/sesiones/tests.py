from django.test import TestCase
from models import user
# Create your tests here.
def test_usuario(): # esta funcion permite realizar el testeo de la existencia del usuario segun su nombre 
    status = True
    try : 
        testeador = user.objects.values_list('nombre')
        print(str(testeador))
        status = True
    except : 
        status = False
    return testeador

class prueba_general(unittest.TestCase):#esta prueba realiza una query mostrando las peliculas existentes en la base de datos
    def testeo_pelicula(self):
        self.assertTrue(test_peli()) 
class prueba_general_autor(unittest.TestCase):#esta prueba realiza una query mostrando los autores existentes en la base de datos
    def testeo_autor(self):
        self.assertTrue(test_autor())
class prueba_general_usuario(unittest.TestCase):#esta prueba realiza una query mostrando los usuarios existentes en la base de datos
    def testeo_usuario(self):
        self.assertTrue(test_usuario())