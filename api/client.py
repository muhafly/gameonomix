import requests
import time
endpoint = "http://gameonomix.com/"
tic = time.perf_counter()
get_response = requests.get(endpoint, json={"level": 0, "habit": 31})
toc = time.perf_counter()
print(f"API responded in {toc - tic:0.4f} seconds")
print(get_response.json())
