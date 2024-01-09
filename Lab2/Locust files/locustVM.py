import time
from locust import HttpUser, task, between

class NumericalIntegrationUser(HttpUser):
    host = "http://13.94.243.23:5000/"  # Specify the base host
    


    @task
    def numerical_integration_task(self):
        lower_bound = 0
        upper_bound = 3.14159
        url = f"/numericalintegralservice/{lower_bound}/{upper_bound}"

        self.client.get(url)

    # You can adjust the time between tasks if needed
    wait_time = between(1, 2)