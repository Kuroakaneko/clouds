import time
from locust import HttpUser, task, between

class NumericalIntegrationUser(HttpUser):
    host = "https://my-auzre-function-integrator.azurewebsites.net"  # Specify the base host
    

    @task
    def numerical_integration_task(self):
        lower_bound = 0
        upper_bound = 3.14159
        url = f"/api/HttpFunction?lower={lower_bound}&upper={upper_bound}"

        self.client.get(url)

    # You can adjust the time between tasks if needed
    wait_time = between(1, 2)