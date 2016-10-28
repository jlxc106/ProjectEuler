#include <stdio.h>
#include <iostream>

using namespace std;

int main(){
int sum=1;
int temp;

for(int i =2; i<=20; i++){
	if(i>sum)
		sum=sum*i;
	else{
		int j =1;
		while((j*sum)%i !=0){
		j++;
		}
		sum=sum*j;
	}

//	for(int j=i-1; j>1; j--){
//		while(temp%j == 0)
//			temp = temp/j;
//	}
//	sum = sum * temp;
}
//int i = 1*2*3*2*5*7*2*3;

cout << sum << endl;
}
