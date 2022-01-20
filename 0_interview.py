

class Number(object):

    def add(sef, a, b):
        return a+b
    def multify(self, a, b):
        return a*b

class Number2(Number):
    def __init__(self):
        super(Number.__init__)

    def return_to_list(self)
        return [str(self.a+self.b), str(self.a*self.b)]
    
    def return_to_list_2(self):
        return [str(self.add()), str(self.multify())]


class TestNumber2()
    def testsetup(self)
        self.a=3
        self.b=5

    def test_add(self):
        AsserEqual(self.a, 8)

    def test_mulitify(self):
        AsserEqual(self.b, 15)
        
    @XXXX.py
    def test_mock(self, mock):
        return_to_list_2.return_value = 0
        AsserEqual(return_to_list, [8,15])

A = Number()
B = A.add(3,5)
C = A. multify(3,5)
AsserEqual(B, 8)
AsserEqual(C, 15)
