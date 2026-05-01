import os
import sys
import subprocess

def check_venv(expected_name):
    venv = os.environ.get("VIRTUAL_ENV")
    if not venv or expected_name not in venv:
        raise EnvironmentError("Script must be run inside the correct virtual environment")
    print(f"Running inside virtual environment: {venv}")

def install_requirements():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def show_save():
    result = subprocess.run([sys.executable, "-m", "pip", "freeze"], capture_output=True, text=True)
    print(result.stdout)
    with open("requirements.txt", "w") as f:
        f.write(result.stdout)

if __name__ == "__main__":
    check_venv("hassleca_2")
    install_requirements()
    show_save()
