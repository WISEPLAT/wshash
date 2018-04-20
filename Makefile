.PHONY: clean test
test:
	./test/test.sh

clean:
	rm -rf *.so pywshash.egg-info/ build/ test/python/python-virtual-env/ test/c/build/ pywshash.so test/python/*.pyc dist/ MANIFEST
