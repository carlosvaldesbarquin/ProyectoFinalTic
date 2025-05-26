import os
import time
import psutil
import subprocess
import json

RESULTS_DIR = "/app/results_docker"
os.makedirs(RESULTS_DIR, exist_ok=True)

def log_sysinfo(label):
    info = {
        "label": label,
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory()._asdict(),
        "disk": psutil.disk_usage("/")._asdict(),
        "timestamp": time.time()
    }
    return info

def run_sysbench_cpu():
    print("▶️ Running sysbench CPU test...")
    result = subprocess.run(["sysbench", "cpu", "--cpu-max-prime=20000", "run"], capture_output=True, text=True)
    return result.stdout

def run_sysbench_memory():
    print("▶️ Running sysbench memory test...")
    result = subprocess.run(["sysbench", "memory", "run"], capture_output=True, text=True)
    return result.stdout

def run_sysbench_disk():
    print("▶️ Preparing disk benchmark...")
    subprocess.run(["sysbench", "fileio", "--file-total-size=1G", "prepare"])
    print("▶️ Running disk I/O benchmark...")
    result = subprocess.run(["sysbench", "fileio", "--file-total-size=1G", "--file-test-mode=seqrd", "run"], capture_output=True, text=True)
    subprocess.run(["sysbench", "fileio", "--file-total-size=1G", "cleanup"])
    return result.stdout

def save_output(label, content):
    file_path = os.path.join(RESULTS_DIR, f"{label}_docker.txt")
    with open(file_path, "w") as f:
        f.write(content)

def save_metrics_json(label, data):
    file_path = os.path.join(RESULTS_DIR, f"{label}_metrics.json")
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def main():
    print("📦 Starting Docker benchmark...")
    metrics_before = log_sysinfo("docker_before")

    cpu_result = run_sysbench_cpu()
    mem_result = run_sysbench_memory()
    disk_result = run_sysbench_disk()

    metrics_after = log_sysinfo("docker_after")

    save_output("cpu_test", cpu_result)
    save_output("memory_test", mem_result)
    save_output("disk_test", disk_result)
    save_metrics_json("docker_before", metrics_before)
    save_metrics_json("docker_after", metrics_after)

    print("✅ Docker benchmark complete. Results saved.")

if __name__ == "__main__":
    main()
