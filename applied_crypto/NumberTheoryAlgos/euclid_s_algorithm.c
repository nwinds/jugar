// returns gcd of x and y
#include "stdlib.h"
#include "stdio.h"
#include "string.h"
#include "errno.h"

int gcd(int x, int y)
{
	int g;
	if(x < 0){
		x = -x;
	}
	if(y < 0){
		y = -y;
	}

	if(x + y == 0){
		fprintf(stderr,"ERROR");
	}

	g = y;

	while(x > 0){
		g = x;
		x = y % x;
		y = g;
	}

	return g;
}

// return the gcd of x1, x2...xm
int multiple_gcd(int m, int *x)
{
	size_t i;
	int g;
	if(m < 1){
		return 0;
	}
	g = x[0];
	for(i = 0; i < m; i++){
		g = gcd(g, x[i]);
		// optimization, since for random x[i], g == 1 60%of the time:
		if(g == 1){
			return 1;
		}
	}

	return g;
}
