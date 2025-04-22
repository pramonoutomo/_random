import os
import random
import datetime
import subprocess

# Set up repo details
REPO_PATH = "D:\Workspaces\Github-Repository\_random"  # Change this to the location of your cloned repo
FILE_PATH = os.path.join(REPO_PATH, "random_data.txt")  # Target file
GIT_USERNAME = "pramonoutomo"
GIT_REPO = "_random"

def update_file():
    """Generate random data and update the file."""
    with open(FILE_PATH, "w") as f:
        f.write(f"Random update: {random.randint(1, 1000)} at {datetime.datetime.now()}")

def commit_and_push():
    """Commit and push changes to GitHub."""
    subprocess.run(["git", "-C", REPO_PATH, "add", FILE_PATH])
    subprocess.run(["git", "-C", REPO_PATH, "commit", "-m", "Automated random update"])
    subprocess.run(["git", "-C", REPO_PATH, "push", "origin", "main"])

if __name__ == "__main__":
    update_file()
    commit_and_push()