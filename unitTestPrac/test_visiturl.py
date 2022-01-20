import unittest
import mock
import visiturl


class TestClient(unittest.TestCase):
    def test_success_request(self):
        # succes_send = mock.Mock(return_value='200')  # way 1: use mock
        # visiturl.send_requests = succes_send
        # self.assertEqual(visiturl.visit_ustack(), '200')

        # visiturl.send_requests = mock.Mock()
        # visiturl.visit_ustack()
        # self.assertEqual(visiturl.send_requests.called, True)  # check if mock object called
        # call_args = visiturl.send_requests.call_args
        # print(call_args[0][0])
        # self.assertIsInstance(call_args[0][0], str)

        status_code = '200'  # way 2: use patch
        success_send = mock.Mock(return_value='200')
        # 使用patch或者patch.object的目的是為了控制mock的範圍，意思就是在一個函式範圍內，或者一個類的範圍內，
        # 或者with語句的範圍內mock掉一個物件。我們看個程式碼例子即可
        with mock.patch('visiturl.send_requests', success_send):
            from visiturl import visit_ustack
            self.assertEqual(visit_ustack(), status_code)

    def test_fail_request(self):
        # fail_send = mock.Mock(return_value='404')
        # visiturl.send_requests = fail_send
        # self.assertEqual(visiturl.visit_ustack(), '404')

        status_code = '404'
        fail_send = mock.Mock(return_value='404')
        with mock.patch.object(visiturl, 'send_requests', fail_send):  # way 3: use patch.object
            from visiturl import visit_ustack
            self.assertEqual(visit_ustack(), status_code)


class Document(unittest.TestCase):
    def method(self):
        self.somthing(1, 2, 3)

    def somthing(self, a, b, c):
        pass


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.makeSuite(TestClient, 'request')
    # suite.addTest(Document())
    # result = unittest.TextTestRunner(verbosity=2).run(suite)
