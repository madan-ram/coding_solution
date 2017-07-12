#include <math.h>
#include "encrypt.h"

int encrypt(int x,int n,int text)
{
	return (( (int) pow(text,x) )%n);
}