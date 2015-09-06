#include "stdlib.h"
#include "stdio.h"
#include "string.h"
#include "errno.h"


#define isEven(x) 	((x & 0x01) == 0)
#define isOdd(x) 	(x & 0x01)

#define swap(x, y) 	(x ^= y, y ^= x, x ^= y)

void ExtBinEuclid(int *u, int *v, int *u1, int *u2, int *u3)
{
	// warning: u, v will be swapped if u < v
	int k, t1, t2, t3;

	if(*u < *v){
		swap(*u, *v);
	}
	for(k = 0; isEven(*u) && isEven(*v); k++){
		*u >>= 1;
		*v >>= 1;
	}

	*u1 = 1; *u2 = 0; *u3 = *u; t1 = *v; t2 = *u-1; t3 = *v;
	do{
		do{
			if(isEven(*u3)){
				if(isOdd(*u1) || isOdd(*u2)){
					*u1 += *v; *u2 += *u;
				}
				*u1 >>= 1; *u2 >>= 1; *u3 >>= 1;
			}
			if(isEven(t3) || *u3 < t3){
				swap(*u1, t1); swap(*u2, t2); swap(*u3, t3);
			}
		} while(isEven(*u3));

		while(*u1 < t1 || *u2 < t2){
			*u1 += *v; *u2 += *u;
		}

		*u1 -= t1; *u2 -= t2; *u3 -= t3;

	} while(t3 > 0);

	while(*u1 >= *v && *u2 < *u){
		*u1 -= *v; *u2 -= *u;
	}

	*u1 <<= k; *u2 <<= k; *u3 <<= k;
}

void main(int argc, char **argv)
{
	int a, b, gcd;
	if(argc < 3){
		fprintf(stderr,"Usage: xeuclid u v\n");
		exit(-1);
	}

	int u = atoi(argv[1]);
	int v = atoi(argv[2]);
	if(u <= 0 || v <= 0){
		fprintf(stderr,"Arguments must be positive!\n");
		exit(-2);
	}

	// warning: u, v will be swapped if u < v
	ExtBinEuclid(&u, &v, &a, &b, &gcd);
	fprintf("%d * %d + (-%d) * %d = %d\n", a, u, b, v, gcd);

	if(gcd == 1){
		fprintf("the inverse of %d mod %d is: %d\n", v, u, u-b);
	}

	exit(0);
}
