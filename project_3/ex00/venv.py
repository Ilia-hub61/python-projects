import os

def virtual_env():
    venv = os.environ.get('VIRTUAL_ENV')
    if venv:
        print(f"Your current virtual env is {venv}")
    else:
        print("No virtual environment active.")

if __name__ == "__main__":
    virtual_env()
