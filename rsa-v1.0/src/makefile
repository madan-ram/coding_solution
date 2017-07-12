CC=gcc
CCFLAGES=-Wall
LIBS=-lm
rsa:main.o prime.o gcd.o encrypt.o decrypt.o
	$(CC) $(CCFLAGES) main.o prime.o gcd.o encrypt.o decrypt.o -o rsa $(LIBS)
main.o:prime.h encrypt.h main.c
	$(CC) $(CCFLAGES) -c main.c

prime.o:prime.h prime.c
	$(CC) $(CCFLAGES) -c prime.c

gcd.o:gcd.h gcd.c
	$(CC) $(CCFLAGES) -c gcd.c

encrypt.o:encrypt.h encrypt.c
	$(CC) $(CCFLAGES) -c encrypt.c

decrypt.o:decrypt.h decrypt.c
	$(CC) $(CCFLAGES) -c decrypt.c

.PHONY: clean
clean:
	rm *.o
