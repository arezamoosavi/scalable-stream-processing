import uuid
import time
from locust import HttpUser, TaskSet, task, between


class UserBehavior(TaskSet):
    @task(1)
    def call_pen_test(self):
        data = {"user_id": str(uuid.uuid4().hex), "cur_time": str(time.time())}
        self.client.post("/produce/pen_test", data)


class User(HttpUser):
    tasks = [
        UserBehavior,
    ]
    host = "http://localhost:8080"
    wait_time = between(1, 3)
