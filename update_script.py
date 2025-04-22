import random
import datetime

FILE_PATH = "random_data.txt"  # File inside the repo

def update_file():
    """Generate random data and update the file."""
    with open(FILE_PATH, "w") as f:
        f.write(f"Random update: {random.randint(1, 1000)} at {datetime.datetime.now()}")

if __name__ == "__main__":
    update_file()