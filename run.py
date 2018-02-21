import subprocess
import signal
import os
import sys

import pytest

def integration_test():
    command = ["coverage", "run", "--source", "myapp", "myapp/myapp.py"]
    server = subprocess.Popen(command, stderr = subprocess.PIPE)

    for line in server.stderr:
        if line.startswith(b' * Running on'):
            break

    pytest.main()

    os.kill(server.pid, signal.SIGINT)
    if not server.poll():
        print("Process correctly halted")

    for line in server.stderr:
        sys.stdout.write(line.decode("utf-8"))

if __name__ == '__main__':
    integration_test()
