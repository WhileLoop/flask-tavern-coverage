# flask-tavern-coverage
Automated API integration testing of Flask application with full code coverage using Tavern and Coverage

run `make` to start the server and execute the test suite. Server is started as pytest fixture and cleanly shutdown using SIGINT allowing coverage to work properly.

report is at `htmlcov/index.html`

See https://taverntesting.github.io/
