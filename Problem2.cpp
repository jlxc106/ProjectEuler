#include <stdio.h>
#include <iostream>

using namespace std;

int main(void){
	int sum =0;
	int x=0;
	int y =1;
	int temp =1;
	while(temp <=4000000){
		if(temp%2==0){
			sum += temp;
		}
		x=y;
		y=temp;
		temp = (x+y);
	}

	cout << sum << endl;
}
