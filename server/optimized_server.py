import subprocess
import time
import requests

MODEL="Qwen/Qwen2.5-0.5B"

server_proc=subprocess.Popen(
    [
        "vllm",
        "serve",
        MODEL,

        "--dtype","half",

        "--gpu-memory-utilization","0.95",

        "--max-num-seqs","64",

        "--max-model-len","1024",

        "--enable-prefix-caching",

        "--disable-log-requests",

        "--disable-log-stats"
    ],
    stdout=open("server_optimized.log","w"),
    stderr=subprocess.STDOUT,
)

print(f"Starting Optimized Server PID: {server_proc.pid}")

url="http://localhost:8000/v1/models"

while True:
    try:
        r=requests.get(url,timeout=2)

        if r.status_code==200:
            print("✅ Optimized server is up and running!")
            break

    except requests.exceptions.RequestException:
        pass

    time.sleep(2)

print("Optimized server ready.")

try:
    while True:
        time.sleep(60)

except KeyboardInterrupt:
    print("Stopping server...")
    server_proc.terminate()
    server_proc.wait()