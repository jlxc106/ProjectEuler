#include <stdio.h>
#include <iostream>


using namespace std;
int main()
{

long long int num = 600851475143;
long long int largest;
int count;
long long int i=2;
while(i<=num){
	if(num%i==0){
		num=(num/i);
		//check if i is a prime number
	}
	else i++;
}
if(i>num)
	cout << "i: " << i<< endl;
else cout<<"num: " << num<<endl;
}
