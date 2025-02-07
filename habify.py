import os
import requests
import subprocess
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Habitica API credentials from environment
HABITICA_USER_ID = os.getenv("HABITICA_USER_ID")
HABITICA_API_TOKEN = os.getenv("HABITICA_API_TOKEN")
HABITICA_API_URL = "https://habitica.com/api/v3/tasks/user"

HEADERS = {
    "x-api-user": HABITICA_USER_ID,
    "x-api-key": HABITICA_API_TOKEN,
    "Content-Type": "application/json"
}

def fetch_tasks():
    """Fetches user tasks from Habitica API."""
    try:
        response = requests.get(HABITICA_API_URL, headers=HEADERS)
        response.raise_for_status()
        tasks = response.json().get("data", [])
        return tasks
    except requests.exceptions.RequestException as e:
        notify("Error", f"Failed to fetch tasks: {e}")
        return []

def get_pending_tasks(tasks):
    """Filters tasks to find pending dailies or incomplete todos."""
    pending = [task["text"] for task in tasks if task["type"] in ["daily", "todo"] and not task["completed"]]
    return pending

def notify(title, message):
    """Sends a desktop notification using notify-send."""
    subprocess.run(["notify-send", title, message])

def main():
    tasks = fetch_tasks()
    pending = get_pending_tasks(tasks)
    
    if pending:
        task_list = "\n".join(pending)
        notify("Habify Reminder - Habitica", f"\n🔴 You have pending tasks 🔴:\n\n{task_list}")
    else:
        notify("Habify Reminder - Habitica", "✅ You're all caught up! ✅")

if __name__ == "__main__":
    main()

