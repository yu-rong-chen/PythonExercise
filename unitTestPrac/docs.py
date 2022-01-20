import unittest
from unittest.mock import MagicMock
from unittest.mock import Mock
from unittest.mock import patch
from student import Student


class ProductionClass:
    def method(self):
        self.somthing(1, 2, 3)

    def somthing(self, a, b, c):
        pass

    def closer(self, somthing):
        somthing.close

    def some_function():
        instance = Student('Robin', 'Wills', 25000)
        instance_mail = instance.mail()
        return instance_mail.method()


if __name__ == '__main__':
    real = ProductionClass()
    # real.somthing = MagicMock()
    # real.method()
    # real.somthing.assert_called_once_with(1, 2, 3)  # to check that it was called with the correct arguments.

    # mock = Mock()
    # real.closer(mock)
    # mock.close.assert_called_with()

    with patch('student.Student.mail') as mock:
        instance = mock.return_value
        instance.method.return_value = 'the result'
        result = ProductionClass.some_function()
        unittest.TestCase.assertEqual(instance.method.return_value(), result)
