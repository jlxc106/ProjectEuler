#include <stdio.h>
#include <iostream>

using namespace std;

int main(){

	int mult=1;
	int temp;

	for(int i = 1; i <= 20; i++)
	{
		if(i>mult)
			mult=mult*i;
		else{
			int j =1;
			while((j*mult)%i !=0) {
				j++;
			}
			mult = mult * j;
		}
	}
	cout << mult << endl;
}
