import pytest
import subprocess, signal, os, sys, socket, time

def wait_for_port(host, port, tries = 60, interval = 1):
    for _ in range(tries):
        try:
            with socket.create_connection((host, port)):
                return True
        except OSError:
            sys.stdout.write('.')
            time.sleep(interval)
    return False


def is_port_available(host, port):
        try:
            with socket.create_connection((host, port)):
                return False
        except OSError:
            return True

@pytest.fixture(scope = "session", autouse = True)
def flask_server_coverage():
    print()
    sys.stdout.write("Starting server")
    if not is_port_available(host = '127.0.0.1', port = 8080):
        raise Exception('Port in use.')

    command = ["coverage", "run", "--source", "myapp", "myapp/myapp.py"]
    server = subprocess.Popen(command, stderr = subprocess.PIPE)

    if not wait_for_port(host = '127.0.0.1', port = 8080):
        raise Exception('Timed out waiting for server.')

    yield

    os.kill(server.pid, signal.SIGINT)
    if not server.poll():
        print()
        print("Server cleanly shutdown")

    print("Server output:")
    for line in server.stderr:
        sys.stdout.write(line.decode("utf-8"))
