#include <stdio.h>
#include <iostream>

using namespace std;

bool test(int b){
	int array[6] = { 0 }; 
	//for(int lengthCount=0; b!=0; b /=10, lengthCount++);
	//lengthCount
	for(int i =0; i< 6; i++){
		array[i]=b%10;
		b=b/10;
	}
	if(array[5]==0){
		if(array[4]==array[0]){
			if(array[3]==array[1]){
				return true;
			}
		}
	}
	else{
		if(array[5]==array[0]){
			if(array[4]==array[1]){
				if(array[3]==array[2])
					return true;
			}
		}
	}
	return false;
}

int main(void){
	int b;
	int max=0;
	for(int i =999; i >=100; i--){
		for(int j=999; j >=100; j--){
			b = i * j;
			if(test(b)){
				if(max<b){
					max = b;
				}
			}
		}
	}
	cout << max << endl;
}
