from locust import HttpUser, TaskSet, task, between


class UserBehavior(TaskSet):
    @task(1)
    def call_pen_test(self):
        self.client.get("/produce/pen_test")


class User(HttpUser):
    tasks = [
        UserBehavior,
    ]
    host = "http://localhost:8080"
    wait_time = between(1, 3)
