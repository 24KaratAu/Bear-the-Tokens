import subprocess

benchmark_cmd=[
    "vllm",
    "bench",
    "serve",

    "--backend","openai",

    "--base-url","http://localhost:8000/v1",

    "--endpoint","/completions",

    "--model","Qwen/Qwen2.5-0.5B",

    "--tokenizer","Qwen/Qwen2.5-0.5B",

    "--max-concurrency","32",

    "--num-prompts","200",

    "--ignore-eos",

    "--random-input-len","512",

    "--random-output-len","512",

    "--save-result",

    "--result-dir","./results",

    "--result-filename","benchmark.json",

    "--temperature","0",

    "--label","optimized"
]

subprocess.run(benchmark_cmd)