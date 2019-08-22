
# coding: utf-8

# In[ ]:


import unittest
import calc

def InteresSimple(C,i,t):
    return C+(C*(i/100)*t)

class TestCalc(unittest.TestCase):
    def test_1(self):
        resultado = InteresSimple(100, 1,1)
        self.assertEqual(resultado,102)

