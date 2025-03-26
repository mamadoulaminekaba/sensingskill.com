#!/usr/bin/env python3
"""
run_pipeline.py
Master script to run AI knowledge pipeline fetchers
"""

import os
import subprocess
from datetime import datetime

# Timestamp for logging
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
logfile = "../datasets/pipeline_run.log"

def log(message):
    with open(logfile, "a") as logf:
        logf.write(f"[{timestamp}] {message}\n")
    print(message)

# Define each fetch script path
scripts = [
    "fetch_wikipedia.py",
    "fetch_wikidata.py",
    "fetch_loc.py"
]

log("🚀 Starting AI knowledge pipeline...")

for script in scripts:
    path = f"./{script}"
    log(f"Running {script}...")
    try:
        subprocess.run(["python3", path], check=True, cwd="./")
        log(f"✅ {script} completed.")
    except subprocess.CalledProcessError as e:
        log(f"❌ Error running {script}: {e}")

log("✅ Pipeline run completed.\n")
