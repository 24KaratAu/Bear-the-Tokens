import subprocess
import time
import requests

MODEL="Qwen/Qwen2.5-0.5B"

server_proc=subprocess.Popen(
    [
        "vllm",
        "serve",
        MODEL
    ],
    stdout=open("server_baseline.log","w"),
    stderr=subprocess.STDOUT,
)

print(f"Starting Server PID: {server_proc.pid}")

url="http://localhost:8000/v1/models"

while True:
    try:
        r=requests.get(url,timeout=2)

        if r.status_code==200:
            print("✅ Server is up and running!")
            break

    except requests.exceptions.RequestException:
        pass

    time.sleep(2)

print("Baseline server ready.")

try:
    while True:
        time.sleep(60)

except KeyboardInterrupt:
    print("Stopping server...")
    server_proc.terminate()
    server_proc.wait()