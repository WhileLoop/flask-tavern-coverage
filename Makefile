all: clean test

clean:
	rm -rf htmlcov
	rm -rf .coverage

test:
	pytest test
	coverage html --fail-under 100
	@echo "Success!"

.PHONY: test
