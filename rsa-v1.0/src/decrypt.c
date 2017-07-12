#include <math.h>
#include "decrypt.h"
int decrypted(int y,int n,int cyphertext)
{
	return (( (int) pow(cyphertext,y) )%n);
}