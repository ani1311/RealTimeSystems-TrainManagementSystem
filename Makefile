VERBOSE=0

all:
	make build
	make run
	make clean

build:
	g++ main.c uiUtils.c trainUtil.c serialPortUtil.c -o a

run:
	./a

clean:
	rm -rf *o a
