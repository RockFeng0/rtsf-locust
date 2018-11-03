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

# import unittest, os
# from httplocust import locusts
# 
# class TestLocusts(unittest.TestCase):
#     
#     def test_parse_locustfile(self):
#         f = locusts.parse_locustfile(r'data\test_locust.yaml')        
#         self.assertTrue(os.path.isfile(f))
#         
# if __name__ == "__main__":
#     unittest.main()

from locust import HttpLocust, TaskSet, task

def jobs_sa(l):
    # 默认情况下，response返回200那么就算事务成功。这个示例，定制事务成功条件：
    # locust的with上下文，需要开启catch_response=True，默认为False
    with l.client.get('https://www.baidu.com',
        catch_response=True,
        name=u'查询作业[PTC-1]') as resp:
        
        if 'resultCode":0' in resp.text:            
            resp.success();# 响应体，包含 resultCode":0 事务成功
            print("-------------")
        else:
            resp.failure('Do not contain: resultCode":0')
            print("++++++++++++")
            return

class Root_sa(TaskSet):
    tasks = [jobs_sa]

class WebsiteUser_sa(HttpLocust):
    task_set = Root_sa
    host = 'http://192.168.109.247'
    min_wait = 500
    max_wait = 1000