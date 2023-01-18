import requests
import time
endpoint = "https://gameonomix.herokuapp.com/"
tic = time.perf_counter()
get_response = requests.get(endpoint, json={"level": 3, "habit": 2})
toc = time.perf_counter()
print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")
print(get_response.json())
