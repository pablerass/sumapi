# -*- coding: utf-8 -*-
from tornado.testing import AsyncHTTPTestCase

import sumapi


class SumapiTest(AsyncHTTPTestCase):
    def get_app(self):
        return sumapi.application()

    def test_sumapi_version(self):
        response = self.fetch('/version', method='GET')
        self.assertEqual(sumapi.__version__, response.body.decode())

    def test_sumapi_sum(self):
        response = self.fetch('/1+2', method='GET')
        self.assertEqual('3', response.body.decode())
        response = self.fetch('/10+3', method='GET')
        self.assertEqual('13', response.body.decode())
        response = self.fetch('/33+4', method='GET')
        self.assertEqual('37', response.body.decode())


    def test_sumapi_mult(self):
        response = self.fetch('/1*2', method='GET')
        self.assertEqual('2', response.body.decode())
        response = self.fetch('/10*3', method='GET')
        self.assertEqual('30', response.body.decode())
        response = self.fetch('/33*4', method='GET')
        self.assertEqual('132', response.body.decode())


if __name__ == '__main__':
    unittest.main()