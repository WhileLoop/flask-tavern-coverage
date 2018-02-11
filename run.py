import subprocess
import signal
import os
from tavern.core import run

def integration_test():
    command = ["coverage", "run", "--source", "myapp", "myapp/myapp.py"]
    server = subprocess.Popen(command, stderr = subprocess.PIPE)

    for line in server.stderr:
        if line.startswith(b' * Running on'):
            break

    success = run("test_server.tavern.yaml", {})
    if not success:
        print("Error running tests")

    os.kill(server.pid, signal.SIGINT)
    if not server.poll():
        print("Process correctly halted")

    subprocess.Popen(["coverage", "html"])


if __name__ == '__main__':
    integration_test()
