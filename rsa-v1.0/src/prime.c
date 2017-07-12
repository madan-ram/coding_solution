#include <stdio.h>
#include "prime.h"
#include "gcd.h"

short int isprime(int num)
{
	int i;
	for(i=2;i<num;i++)
	{
		if(num%i==0)
		{
			return 0;
		}
	}
	return 1;
}

short int iscoprime(int x,int z,char *message)
{
	if(x<=1 || x>=z)
	{
		sprintf(message,"ERROR:%d is not in between 1 and %d",x,z);
		return 0;
	}
	else
	{
		if(gcd(x,z)!=1)
		{
			sprintf(message,"ERROR:gcd(%d,%d)!=1",x,z);
			return 0;	
		}
	}
	return 1;
}