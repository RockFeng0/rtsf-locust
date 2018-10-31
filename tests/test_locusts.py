#! python3
# -*- encoding: utf-8 -*-
'''
Current module: tests.test_locusts

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:     luokefeng@163.com
    RCS:      tests.test_locusts,  v1.0 2018年10月24日
    FROM:   2018年10月24日
********************************************************************
======================================================================

Provide a function for the automation test

'''

import unittest, os
from httplocust import locusts

class TestLocusts(unittest.TestCase):
    
    def test_parse_locustfile(self):
        f = locusts.parse_locustfile(r'data\test_locust.yaml')        
        self.assertTrue(os.path.isfile(f))
        
if __name__ == "__main__":
    unittest.main()