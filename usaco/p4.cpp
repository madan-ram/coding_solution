/*
ID: madan_r2
LANG: C++
TASK: friday
*/
#include <stdio.h>
#include <iostream>

using namespace std;
bool is_leap_year(int y) {
	//if centure year the see if divisible by 400 if not then it is not leap year
	if(y%100 == 0) {
		return (y%400 == 0);
	}
	return (y%4 == 0);

}

int main(int args, char **argv) {
	FILE *fin = fopen("friday.in", "r");
	FILE *fout = fopen("friday.out", "w");
	int N;
	int day[7] = {0, 0, 0, 0, 0, 0, 0};
	long int days_in_month_till_13[12] = {13, 44, 72, 103, 133, 164, 194, 225, 256, 286, 317, 347};
	fscanf(fin, "%d", &N);
	for(int y=1900; y<(1900+N); y++) {
		for(int i=0; i<12; i++) {
			int day_index = (days_in_month_till_13[i]+((y-1900)*365))%7;
			day[day_index] += 1;
			if(i == 1 && is_leap_year(y)) {
				for(int j=0; j<12; j++) {
					days_in_month_till_13[j] += 1;
				}
			}
		}
	}

	fprintf(fout,"%d ", day[6]);
	for(int i=0; i<5; i++) {
		fprintf(fout,"%d ", day[i]);
	}
	fprintf(fout,"%d", day[5]);
	fprintf(fout, "\n");
	return 0;
}