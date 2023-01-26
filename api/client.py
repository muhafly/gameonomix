import requests
import time
# endpoint = "http://gameonomix.com/"
endpoint = "http://localhost:8000/"
tic = time.perf_counter()
get_response = requests.get(endpoint, json={"level": 9, "habit": 3.2, "event": 1})
toc = time.perf_counter()
print(f"API responded in {toc - tic:0.4f} seconds")
print(get_response.json())
