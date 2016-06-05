/*
ID: madan_r2
LANG: C
TASK: ride
*/
#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
	int i=0;
	FILE *fin = fopen("ride.in", "r");
	FILE *fount = fopen("ride.out", "w");
	char comet_str[7], group_str[7];
	long int  comet_id=1, group_id=1;
	fscanf(fin, "%s\n%s", &comet_str[0], &group_str[0]);

	for(i=0; i<strlen(comet_str); i++) {
		comet_id *= (short) comet_str[i] - 64;
		printf("%d\n", (short) comet_str[i] - 64);
	} 
	printf("------------------\n");
	for(i=0; i<strlen(group_str); i++) {
		group_id *= (short) group_str[i] - 64;
		printf("%d\n", (short) group_str[i] - 64);
	}
	if(comet_id%47 == group_id%47) {
		fprintf(fount, "GO\n");
	} else {
		fprintf(fount, "STAY\n");
	}
	printf("------------------\n");
	printf("%ld\n", group_id%47);
	printf("%ld\n", comet_id%47);
	return 0;
}