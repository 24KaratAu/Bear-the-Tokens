import requests

try:
    requests.post("http://localhost:8000/shutdown")

except:
    print("Server already stopped.")