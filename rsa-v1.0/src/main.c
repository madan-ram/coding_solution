#include <stdio.h>
#include "prime.h"
#include "encrypt.h"
#include "decrypt.h"

int main(int argc,char **argv)
{
	int a,b;
	int z,x,y,n,text;
	int cyphertext;
	char message[40];
	
	//Choose two distinct prime numbers a and b. 
	printf("enter the prime number a and b\n");
	scanf("%d",&a);
	scanf("%d",&b);
	
	if(isprime(a)==0)
	{
		printf("%d is not a prime number\n",a);
		return 0;
	}
	else if(isprime(b)==0)
	{
		printf("%d is not a prime number\n",b);
		return 0;
	}
	
	n=a*b;
	z=(a-1)*(b-1);

	//Choose an integer e such that 1 < x < z and gcd(e, z) = 1; i.e. x and z are coprime(relatively prime). 
	printf("enter the value of x(encruption key)\n");
	scanf("%d",&x);

	if(iscoprime(x,z,message)==0)
	{
		printf("%s\n",message);
		return 0;
	}
	y=1;
	while(1)
	{
		if(((y*x)-1)%z==0)
		{
			break;
		}
		y++;
	}

	//the public key is {x,n} is created
	//the private key is {y,n} is created
	printf("enter the message to encrupt\n");
	scanf("%d",&text);
	//text is encryptred
	cyphertext=encrypt(x,n,text);
	printf("the encrupt text is %d \n",cyphertext);

	printf("%d=y\n",y );

	//cyphertext is decrypted
	text=decrypted(y,n,cyphertext);
	printf("the decrypt text is %d \n",text);
	return 0;
}