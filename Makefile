all: clean test

clean:
	rm -rf htmlcov
	rm -f .coverage

test:
	python3 run.py
	coverage html --fail-under 100
	@echo "Success!"

browse:
	"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" htmlcov/index.html

.PHONY: test browse
