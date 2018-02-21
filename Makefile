all: clean test

clean:
	rm -rf htmlcov
	rm -f .coverage

test:
	python3 run.py
	coverage html
	"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" htmlcov/index.html

.PHONY: test
