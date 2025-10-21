import os
import subprocess
from dotenv import load_dotenv
from datetime import datetime

# === CONFIG ===
ENV_PATH = "/home/gost/account/.env"
REPO_PATH = "/home/gost/all-project/git-all/7heBlackLand.github.io"
LOG_FILE = os.path.join("/home/gost/all-project/git-all", "git_actions.log")

# === Load .env ===
load_dotenv(dotenv_path=ENV_PATH)
token = os.getenv("GITHUB_TOKEN")

if not token:
    print("❌ Error: GITHUB_TOKEN not found in .env file.")
    exit(1)

# === Helper Functions ===
def run(cmd, silent=False):
    """Run shell command safely"""
    if not silent:
        print(f"🚀 Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

def log_action(action_text):
    """Write log with timestamp"""
    with open(LOG_FILE, "a") as log:
        log.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {action_text}\n")

# === Ensure repo exists ===
if not os.path.isdir(REPO_PATH):
    print(f"⚠️ Repository not found at:\n   {REPO_PATH}\n")
    print("1️⃣  Clone a new repository")
    print("2️⃣  Cancel / Exit")
    choice = input("\n👉 Enter your choice (1-2): ").strip()

    if choice == "1":
        repo_url = input("\n🌐 Enter GitHub repository URL to clone: ").strip()
        if not repo_url:
            print("❌ No URL provided. Exiting...")
            exit(0)

        # Add token if needed
        if repo_url.startswith("https://") and "@" not in repo_url:
            repo_url = repo_url.replace("https://", f"https://{token}@")

        os.makedirs(os.path.dirname(REPO_PATH), exist_ok=True)
        try:
            run(["git", "clone", repo_url, REPO_PATH])
            print(f"✅ Repository cloned successfully into:\n   {REPO_PATH}\n")
            log_action(f"Cloned repository from {repo_url}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to clone repository: {e}")
            exit(1)
    else:
        print("👋 Cancelled by user. Exiting...")
        exit(0)

# === Change to repo directory ===
os.chdir(REPO_PATH)

# === Configure git identity ===
try:
    run(["git", "config", "user.name", "Auto Commit Bot"], silent=True)
    run(["git", "config", "user.email", "autocommit@example.com"], silent=True)
except subprocess.CalledProcessError:
    print("⚠️ Warning: Could not set git identity.")

# === Fix remote URL with token ===
try:
    origin_url = subprocess.check_output(["git", "remote", "get-url", "origin"], text=True).strip()
    if "@" not in origin_url:
        origin_url = origin_url.replace("https://", f"https://{token}@")
        run(["git", "remote", "set-url", "origin", origin_url], silent=True)
except subprocess.CalledProcessError:
    print("⚠️ Warning: Could not update remote origin URL.")

# === Perform Git Pull ===
try:
    print("\n🔄 Pulling latest changes from GitHub...")
    run(["git", "pull"])
    print("✅ Repository updated successfully!\n")
    log_action("Pulled latest changes from GitHub")
except subprocess.CalledProcessError as e:
    print(f"❌ Git pull failed: {e}\n")
    log_action(f"Git pull failed: {e}")


#git_push.py

import os
import subprocess
from dotenv import load_dotenv
from datetime import datetime

# === CONFIG ===
ENV_PATH = "/home/gost/account/.env"
REPO_PATH = "/home/gost/all-project/git-all/7heBlackLand.github.io"
LOG_FILE = os.path.join("/home/gost/all-project/git-all", "git_actions.log")

# === Load .env ===
load_dotenv(dotenv_path=ENV_PATH)
token = os.getenv("GITHUB_TOKEN")

if not token:
    print("❌ Error: GITHUB_TOKEN not found in .env file.")
    exit(1)

# === Helper Functions ===
def run(cmd, silent=False):
    if not silent:
        print(f"🚀 Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

def log_action(action_text):
    with open(LOG_FILE, "a") as log:
        log.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {action_text}\n")

# === Ensure repo exists ===
if not os.path.isdir(REPO_PATH):
    print(f"❌ Repository not found at {REPO_PATH}. Please clone it first.")
    exit(1)

# === Change to repo directory ===
os.chdir(REPO_PATH)

# === Configure git identity ===
try:
    run(["git", "config", "user.name", "Auto Commit Bot"], silent=True)
    run(["git", "config", "user.email", "autocommit@example.com"], silent=True)
except subprocess.CalledProcessError:
    print("⚠️ Warning: Could not set git identity.")

# === Fix remote URL with token ===
try:
    origin_url = subprocess.check_output(["git", "remote", "get-url", "origin"], text=True).strip()
    if "@" not in origin_url:
        origin_url = origin_url.replace("https://", f"https://{token}@")
        run(["git", "remote", "set-url", "origin", origin_url], silent=True)
except subprocess.CalledProcessError:
    print("⚠️ Warning: Could not update remote origin URL.")

# === Placeholder for your custom Push logic ===
print("\n📦 Ready to push local changes...")
log_action("git_push.py started - ready for push logic")
# 👉 You can now add your `git add .`, `git commit`, and `git push` steps here.

