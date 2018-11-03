# -*- encoding: utf-8 -*-
'''
Current module: Simple_login_3

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      Simple_login_3,v 1.0 2016年11月10日
    FROM:   2016年11月10日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
   
    @task()
    def t_rtsf(self):
        for i in ("rtsf","rtsf-web","rtsf-http","rtsf-win","rtsf-app"):
            with self.client.get('/search/?q={}'.format(i),catch_response=True) as resp:
                if '<title>Search results' in resp.text:            
                    resp.success()
                else:
                    resp.failure('no title')
    
    

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
    host = 'https://pypi.org/'
    