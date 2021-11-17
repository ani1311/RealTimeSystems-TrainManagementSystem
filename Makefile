VERBOSE=0

all:
	make build
	make run
	make clean

build:
	g++ main.c trainUtil.c uiUtils.c serialPortUtil.c -o a

run:
	./a

clean:
	rm -rf *o a
