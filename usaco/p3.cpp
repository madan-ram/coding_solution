/*
ID: madan_r2
LANG: C++
TASK: gift1
*/
#include <iostream>
#include <map>
#include <string.h>
#include <stdio.h>

#define _DEFINE_DEPRECATED_HASH_CLASSES 0

using namespace std;

int main(int argc, char const *argv[])
{
	int group_size;
	int cost_matrix[10];

	/*assigne array to zero*/
	for(int i=0; i<10; i++)
		cost_matrix[i] = 0;

	char name[15];
	char name_list[10][15];
	int giver_id, friend_id;
	int amount, number_of_friends;

	FILE *fin = fopen("gift1.in", "r");
	FILE *fout = fopen("gift1.out", "w");
	map<string, int> index_to_name;

	fscanf(fin, "%d\n", &group_size);
	for(int i=0; i<group_size; i++) {
		fscanf(fin, "%s\n", &name[0]);
		index_to_name[name] = i;
		strcpy(name_list[i], name);
		/*cout<<index_to_name[name]<<endl;*/
	}

	for(int i=0; i<group_size; i++) {
		cout<<name_list[i]<<endl;
	}

	for(int i=0; i<group_size; i++) {
		fscanf(fin, "%s\n", &name[0]);
		giver_id = index_to_name[name];
		fscanf(fin, "%d %d\n", &amount, &number_of_friends);
		if(number_of_friends != 0){
			int left_out = amount%number_of_friends;
			int amount_given = amount - left_out;
			/*calculate the amount given to each friends*/
			int amount_per_friend = amount_given/number_of_friends;
			cost_matrix[giver_id] -= amount_given;
			for(int j=0; j<number_of_friends; j++) {
				fscanf(fin, "%s\n", &name[0]);
				friend_id = index_to_name[name];
				cost_matrix[friend_id] += amount_per_friend;
			}
		}
	}
	for(int i=0; i<group_size; i++) {
		fprintf(fout, "%s %d\n", name_list[i], cost_matrix[index_to_name[name_list[i]]]);
	}
	return 0;
}