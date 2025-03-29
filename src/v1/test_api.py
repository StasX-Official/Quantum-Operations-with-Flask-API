import requests
import time

class APITester:
    def __init__(self, base_url, test_count=10000):
        self.base_url = base_url
        self.test_count = test_count

    def send_post_request(self, endpoint, data):
        try:
            response = requests.post(f"{self.base_url}/{endpoint}", json=data)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error during POST request: {e}")
            return None

    def send_get_request(self, endpoint):
        try:
            response = requests.get(f"{self.base_url}/{endpoint}")
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error during GET request: {e}")
            return None

    def test_register(self):
        for i in range(self.test_count):
            data = {'username': f'user{i}', 'password': f'pass{i}'}
            start = time.time()
            response = self.send_post_request('register', data)
            end = time.time()
            if response:
                print(f"Registration {i+1} | Time: {end - start} seconds | Status: {response.status_code}")

    def test_quantum(self):
        for i in range(self.test_count):
            start = time.time()
            response = self.send_get_request('quantum')
            end = time.time()
            if response:
                print(f"Quantum request {i+1} | Time: {end - start} seconds | Status: {response.status_code}")

    def run_tests(self):
        start = time.time()
        self.test_register()
        end = time.time()
        print("Testing quantum API...")
        start2 = time.time()
        self.test_quantum()
        end2 = time.time()
        print("Testing completed.")
        print(f"Total registration test time: {end - start} seconds. Speed: {self.test_count / (end - start)} requests/second")
        print(f"Total quantum API test time: {end2 - start2} seconds. Speed: {self.test_count / (end2 - start2)} requests/second")


if __name__ == "__main__":
    tester = APITester('http://127.0.0.1:5000')
    tester.run_tests()
