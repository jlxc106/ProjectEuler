#include <stdio.h>
#include <iostream>

using namespace std;
int main()
{

long int num = 600851475143;
long int largest;
int count;
long int i=2;
while(i <= num){
	if(num%i==0){
		num=(num/i);
	}
	else i++;
}
cout << "i: " << i<< endl;
}
