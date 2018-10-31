#coding: utf-8
import zmq
from locust import HttpLocust, TaskSet, task
from httplocust.task import LocustTask

class WebPageTasks(TaskSet):
    def on_start(self):
        self.test_runner = LocustTask(self.locust.file_path, self.client)

    @task
    def test_specified_scenario(self):
        self.test_runner.run()

class WebPageUser(HttpLocust):
    host = ""
    task_set = WebPageTasks
    min_wait = 1000
    max_wait = 5000

    file_path = r"D:\auto\github_repo\rtsf-locust\tests\data\test_locust.yaml"
