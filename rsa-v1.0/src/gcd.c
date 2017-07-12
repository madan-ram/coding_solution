/* "Euclidean algorithm": Recursive Standard C Function: Greatest Common Divisor */
#include "gcd.h"

int gcd(int a,int b)
{
	if(a==0)	return b;
	return gcd(b%a,a);
}